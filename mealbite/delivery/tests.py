from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from delivery.models import Customer, Restaurant, Item, Cart, CartItem


class DeliveryAppTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='password123', email='test@example.com')
        self.customer = Customer.objects.create(
            user=self.user,
            username='testuser',
            email='test@example.com',
            mobile='1234567890',
            address='123 Main St'
        )
        self.restaurant = Restaurant.objects.create(
            name='Test Diner',
            cuisine='American',
            rating=4.5,
            picture='https://example.com/pic.jpg'
        )
        self.item = Item.objects.create(
            restaurant=self.restaurant,
            name='Test Burger',
            description='Juicy burger',
            price=150.0,
            vegeterian=False
        )

    def test_index_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_signup(self):
        response = self.client.post(reverse('signup'), {
            'username': 'newuser',
            'password': 'newpassword',
            'email': 'new@example.com',
            'mobile': '9876543210',
            'address': '456 Oak St'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='newuser').exists())
        self.assertTrue(Customer.objects.filter(username='newuser').exists())

    def test_admin_signup(self):
        response = self.client.post(reverse('signup'), {
            'username': 'admin_manager',
            'password': 'adminpassword',
            'role': 'admin',
            'email': 'admin@example.com',
            'mobile': '9998887770',
            'address': 'Headquarters'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('admin_home'))
        user = User.objects.get(username='admin_manager')
        self.assertTrue(user.is_superuser)

    def test_signin(self):
        response = self.client.post(reverse('signin'), {
            'username': 'testuser',
            'password': 'password123'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('customer_home', kwargs={'username': 'testuser'}))

    def test_add_restaurant(self):
        response = self.client.post(reverse('add_restaurant'), {
            'name': 'New Bistro',
            'picture': 'https://example.com/bistro.jpg',
            'cuisine': 'French',
            'rating': '4.8'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Restaurant.objects.filter(name='New Bistro').exists())

    def test_add_to_cart_and_show_cart(self):
        response = self.client.get(reverse('add_to_cart', kwargs={'item_id': self.item.id, 'username': 'testuser'}))
        self.assertEqual(response.status_code, 302)
        
        cart = Cart.objects.get(customer=self.customer)
        self.assertEqual(cart.cartitem_set.count(), 1)
        self.assertEqual(cart.total_price(), 150.0)

        response = self.client.get(reverse('show_cart', kwargs={'username': 'testuser'}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Burger')

    def test_update_quantity_and_remove_from_cart(self):
        cart = Cart.objects.create(customer=self.customer)
        ci = CartItem.objects.create(cart=cart, item=self.item, quantity=1)

        # Update quantity
        response = self.client.post(reverse('update_quantity', kwargs={'item_id': self.item.id, 'username': 'testuser'}), {'quantity': 3})
        self.assertEqual(response.status_code, 302)
        ci.refresh_from_db()
        self.assertEqual(ci.quantity, 3)

        # Remove item
        response = self.client.post(reverse('remove_from_cart', kwargs={'item_id': self.item.id, 'username': 'testuser'}))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(CartItem.objects.filter(id=ci.id).exists())

    def test_checkout_and_orders(self):
        cart = Cart.objects.create(customer=self.customer)
        CartItem.objects.create(cart=cart, item=self.item, quantity=2)

        response = self.client.get(reverse('checkout', kwargs={'username': 'testuser'}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Checkout')

        response = self.client.get(reverse('orders', kwargs={'username': 'testuser'}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Thank you, testuser!')
        # Ensure cart is cleared after order
        self.assertEqual(cart.cartitem_set.count(), 0)

