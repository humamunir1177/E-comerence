from django.db import models
from django.contrib.auth.models import User


# =========================
# CATEGORY
# =========================
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# =========================
# BRAND
# =========================
class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# =========================
# PRODUCT
# =========================
class Product(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    stock = models.BooleanField(default=True)
    warranty = models.CharField(max_length=100, default="no warranty")
    features = models.TextField(blank=True, null=True)
    popular = models.BooleanField(default=True)
    image = models.ImageField(upload_to='product/', default='default.png')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True, blank=True)
    arrival = models.DateTimeField(auto_now=True)
    price = models.IntegerField()
    discount = models.IntegerField(default=0)

    def discounted_price(self):
        return int(self.price - (self.price * self.discount / 100))

    def __str__(self):
        return self.name


# =========================
# CUSTOMER USER
# =========================
class Customer_user(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.user.username


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='images'
    )
    image = models.ImageField(upload_to='product/gallery/')

    def __str__(self):
        return self.product.name



class ProductSpec(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='specs')
    field = models.CharField(blank=True, max_length=255)
    value = models.TextField(blank=True)

    def __str__(self):
        return f"{self.product.name} - {self.field}"



class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username



class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        return self.product.discounted_price() * self.quantity

    def __str__(self):
        return f"{self.product.name} ({self.quantity})"
