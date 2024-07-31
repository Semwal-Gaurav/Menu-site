# menu/models.py

from django.db import models

class Breakfast(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='food_images/')

    def __str__(self):
        return self.name

class Tandoor_se(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='food_images/')

    def __str__(self):
        return self.name

class Main_course(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='food_images/')

    def __str__(self):
        return self.name

class Mushroom_se(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='food_images/')

    def __str__(self):
        return self.name

class Paneer_se(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='food_images/')

    def __str__(self):
        return self.name

class Snacks(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='food_images/')

    def __str__(self):
        return self.name

class Champ(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='food_images/')

    def __str__(self):
        return self.name

class Salad(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='food_images/')

    def __str__(self):
        return self.name

class Raita(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='food_images/')

    def __str__(self):
        return self.name

class Papad(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='food_images/')

    def __str__(self):
        return self.name

class Pulao_Rice(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='food_images/')

    def __str__(self):
        return self.name

class Dessert_cold_drinks(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='drink_images/')
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name


class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    customer_phone = models.CharField(max_length=15)
    table_number = models.CharField(max_length=10, blank=True, null=True)  # Added table number field
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Pending')

    def __str__(self):
        return f"Order {self.id} by {self.customer_name}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    item_type = models.CharField(max_length=50, default='unknown')
    item_id = models.PositiveIntegerField(default=0)
    quantity = models.PositiveIntegerField()
    name = models.CharField(max_length=100,  default='Unnamed Item')
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.name} x {self.quantity}"