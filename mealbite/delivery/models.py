from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    # Profile information for a Django `User`.
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    mobile = models.CharField(max_length=20)
    address = models.CharField(max_length=300)

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    picture = models.URLField(max_length=500, default='https://bizimages.withfloats.com/actual/3f6bfde19dbe4c178ea34e0e0ae96ad7.jpg')
    cuisine = models.CharField(max_length=200)
    rating = models.FloatField()

class Item(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="items")
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=500)
    price = models.FloatField()
    vegeterian = models.BooleanField(default=False)
    picture = models.URLField(max_length=500, default='https://www.indiafilings.com/learn/wp-content/uploads/2024/08/How-to-Start-Food-Business.jpg')

class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="carts")
    items = models.ManyToManyField("Item", related_name="carts")

    def total_price(self):
        # Prefer CartItem quantities if present, otherwise sum simple M2M
        if hasattr(self, 'cartitem_set') and self.cartitem_set.exists():
            return sum(ci.item.price * ci.quantity for ci in self.cartitem_set.all())
        return sum(item.price for item in self.items.all())


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = (('cart', 'item'),)