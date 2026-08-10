from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, JsonResponse
try:
    import razorpay
except ImportError:
    razorpay = None
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User

from .models import Cart, Customer, Item, Restaurant, CartItem


def get_customer_profile(username):
    """Safely retrieves a Customer profile by username, handling any duplicate records gracefully."""
    customers = Customer.objects.filter(username=username).order_by('-user_id', '-id')
    if customers.exists():
        customer = customers.first()
        if customers.count() > 1:
            for dup in customers[1:]:
                for cart in dup.carts.all():
                    cart.customer = customer
                    cart.save()
                dup.delete()
        return customer
    return Customer.objects.create(
        username=username,
        email=f"{username}@example.com",
        mobile="",
        address=""
    )


def index(request):
    return render(request, "delivery/index.html")


def open_signup(request):
    return render(request, "delivery/signup.html")


def open_signin(request):
    return render(request, "delivery/signin.html")


def signup(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")
        email = request.POST.get("email", "").strip()
        mobile = request.POST.get("mobile", "").strip()
        address = request.POST.get("address", "").strip()
        role = request.POST.get("role", "customer").strip()

        if not username or not password:
            return render(request, 'delivery/signup.html', {'error': 'Username and password are required.'})

        if User.objects.filter(username=username).exists():
            return render(request, 'delivery/signup.html', {'error': 'Username already exists!'})

        # Determine if signing up as admin
        is_admin = role == 'admin' or username.lower() == 'admin' or 'admin' in username.lower()

        if is_admin:
            user = User.objects.create_superuser(username=username, email=email, password=password)
        else:
            user = User.objects.create_user(username=username, email=email, password=password)

        # create or link customer profile safely without duplicates
        customer = Customer.objects.filter(username=username).first()
        if customer:
            customer.user = user
            customer.email = email
            customer.mobile = mobile
            customer.address = address
            customer.save()
        else:
            Customer.objects.create(
                user=user,
                username=username,
                email=email,
                mobile=mobile,
                address=address,
            )

        auth_login(request, user)

        if is_admin or user.is_superuser or user.is_staff:
            return redirect('admin_home')
        return redirect('customer_home', username=username)

    return render(request, 'delivery/signup.html')


def signin(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            if user.is_superuser or username == 'admin':
                return redirect('admin_home')
            return redirect('customer_home', username=username)
        else:
            return render(request, 'delivery/fail.html')

    return render(request, 'delivery/signin.html')


def logout_view(request):
    auth_logout(request)
    return redirect('open_signin')


def open_add_restaurants(request):
    return render(request, "delivery/add_restaurant.html")  


def add_restaurant(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        picture = request.POST.get('picture', '').strip()
        cuisine = request.POST.get('cuisine', '').strip()
        rating_str = request.POST.get('rating', '0')

        try:
            rating = float(rating_str)
        except ValueError:
            rating = 0.0

        if not picture or not (picture.startswith('http://') or picture.startswith('https://')):
            picture = 'https://bizimages.withfloats.com/actual/3f6bfde19dbe4c178ea34e0e0ae96ad7.jpg'

        if Restaurant.objects.filter(name=name).exists():
            return render(request, 'delivery/add_restaurant.html', {'error': 'Restaurant with this name already exists.'})

        Restaurant.objects.create(
            name=name,
            picture=picture,
            cuisine=cuisine,
            rating=rating,
        )
        return redirect('open_show_restaurants')
    return redirect('open_add_restaurants')


def open_show_restaurants(request):
    restaurantList = Restaurant.objects.all()
    return render(request, "delivery/show_restaurants.html", {"restaurantList": restaurantList})


def open_update_restaurant(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    return render(request, 'delivery/update_restaurant.html', {"restaurant": restaurant})


def update_restaurant(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        picture = request.POST.get('picture', '').strip()
        cuisine = request.POST.get('cuisine', '').strip()
        rating_str = request.POST.get('rating')

        if name:
            restaurant.name = name
        if picture:
            if not (picture.startswith('http://') or picture.startswith('https://')):
                picture = 'https://bizimages.withfloats.com/actual/3f6bfde19dbe4c178ea34e0e0ae96ad7.jpg'
            restaurant.picture = picture
        if cuisine:
            restaurant.cuisine = cuisine
        if rating_str:
            try:
                restaurant.rating = float(rating_str)
            except ValueError:
                pass
        restaurant.save()

    return redirect('open_show_restaurants')


def delete_restaurant(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    restaurant.delete()
    return redirect('open_show_restaurants')


def open_update_menu(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    itemList = restaurant.items.all()
    return render(request, 'delivery/update_menu.html', {"itemList": itemList, "restaurant": restaurant})


def update_menu(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        description = request.POST.get('description', '').strip()
        price_str = request.POST.get('price', '0')
        vegeterian = request.POST.get('vegeterian') == 'on'
        picture = request.POST.get('picture', '').strip()

        try:
            price = float(price_str)
        except ValueError:
            price = 0.0

        if not picture or not (picture.startswith('http://') or picture.startswith('https://')):
            picture = 'https://www.indiafilings.com/learn/wp-content/uploads/2024/08/How-to-Start-Food-Business.jpg'

        Item.objects.create(
            restaurant=restaurant,
            name=name,
            description=description,
            price=price,
            vegeterian=vegeterian,
            picture=picture,
        )
    return redirect('open_update_menu', restaurant_id=restaurant_id)


def delete_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    restaurant_id = item.restaurant.id
    item.delete()
    return redirect('open_update_menu', restaurant_id=restaurant_id)


def view_menu(request, restaurant_id, username):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    itemList = restaurant.items.all()
    return render(request, 'delivery/customer_menu.html', {
        "itemList": itemList,
        "restaurant": restaurant,
        "username": username
    })


def customer_home(request, username):
    restaurantList = Restaurant.objects.all()
    return render(request, 'delivery/customer_home.html', {"restaurantList": restaurantList, "username": username})


def admin_home(request):
    restaurant_count = Restaurant.objects.count()
    item_count = Item.objects.count()
    customer_count = Customer.objects.count()
    return render(request, 'delivery/admin_home.html', {
        'restaurant_count': restaurant_count,
        'item_count': item_count,
        'customer_count': customer_count,
    })


def add_to_cart(request, item_id, username):
    item = get_object_or_404(Item, id=item_id)
    customer = get_customer_profile(username)

    cart, _ = Cart.objects.get_or_create(customer=customer)

    cart_item, ci_created = CartItem.objects.get_or_create(cart=cart, item=item)
    if not ci_created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('view_menu', restaurant_id=item.restaurant.id, username=username)


def show_cart(request, username):
    customer = get_customer_profile(username)
    cart = Cart.objects.filter(customer=customer).first()
    cart_items = []
    if cart:
        for ci in cart.cartitem_set.all():
            cart_items.append({'item': ci.item, 'quantity': ci.quantity})
    total_price = cart.total_price() if cart else 0

    return render(request, 'delivery/cart.html', {"cart_items": cart_items, "total_price": total_price, "username": username})


def remove_from_cart(request, item_id, username):
    customer = get_customer_profile(username)
    cart = Cart.objects.filter(customer=customer).first()
    if cart:
        CartItem.objects.filter(cart=cart, item_id=item_id).delete()
    return redirect('show_cart', username=username)


def update_quantity(request, item_id, username):
    if request.method == 'POST':
        try:
            qty = int(request.POST.get('quantity', 1))
        except ValueError:
            qty = 1
        customer = get_customer_profile(username)
        cart = Cart.objects.filter(customer=customer).first()
        if cart:
            try:
                ci = CartItem.objects.get(cart=cart, item_id=item_id)
                if qty <= 0:
                    ci.delete()
                else:
                    ci.quantity = qty
                    ci.save()
            except CartItem.DoesNotExist:
                pass
    return redirect('show_cart', username=username)


def checkout(request, username):
    customer = get_customer_profile(username)
    cart = Cart.objects.filter(customer=customer).first()
    cart_items = cart.cartitem_set.all() if cart else []
    total_price = cart.total_price() if cart else 0

    if total_price == 0:
        return render(request, 'delivery/checkout.html', {
            'error': 'Your cart is empty!',
            'username': username,
        })

    amount_paise = int(total_price * 100)
    key_id = getattr(settings, 'RAZORPAY_KEY_ID', 'rzp_test_TM4IEF2Xa74hU3')
    key_secret = getattr(settings, 'RAZORPAY_KEY_SECRET', 'NHdvLqmhX9cX8is7qw3cCbrR')

    if razorpay:
        try:
            client = razorpay.Client(auth=(key_id, key_secret))
            order_data = {
                'amount': amount_paise,
                'currency': 'INR',
                'payment_capture': '1',
            }
            order = client.order.create(data=order_data)
            order_id = order['id']
        except Exception as e:
            order_id = f"order_demo_{username}"
    else:
        order_id = f"order_demo_{username}"

    return render(request, 'delivery/checkout.html', {
        'username': username,
        'cart_items': cart_items,
        'total_price': total_price,
        'amount_paise': amount_paise,
        'razorpay_key_id': key_id,
        'order_id': order_id,
    })


@csrf_exempt
def verify_payment(request, username):
    if request.method != 'POST':
        return JsonResponse({'error': 'Invalid method'}, status=405)

    payment_id = request.POST.get('razorpay_payment_id')
    order_id = request.POST.get('razorpay_order_id')
    signature = request.POST.get('razorpay_signature')

    key_id = getattr(settings, 'RAZORPAY_KEY_ID', 'rzp_test_TM4IEF2Xa74hU3')
    key_secret = getattr(settings, 'RAZORPAY_KEY_SECRET', 'NHdvLqmhX9cX8is7qw3cCbrR')

    if signature and razorpay and not order_id.startswith('order_demo_'):
        client = razorpay.Client(auth=(key_id, key_secret))
        try:
            params = {
                'razorpay_order_id': order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature,
            }
            client.utility.verify_payment_signature(params)
        except Exception as e:
            return JsonResponse({'status': 'failed', 'error': str(e)}, status=400)

    customer = get_customer_profile(username)
    cart = Cart.objects.filter(customer=customer).first()
    total_price = 0
    if cart:
        total_price = cart.total_price()
        cart.cartitem_set.all().delete()

    return JsonResponse({'status': 'ok', 'total_price': total_price})


def orders(request, username):
    customer = get_customer_profile(username)
    cart = Cart.objects.filter(customer=customer).first()

    cart_items = list(cart.cartitem_set.all()) if cart else []
    total_price = cart.total_price() if cart else 0

    if cart:
        cart.cartitem_set.all().delete()

    return render(request, 'delivery/orders.html', {
        'username': username,
        'customer': customer,
        'cart_items': cart_items,
        'total_price': total_price,
    })
