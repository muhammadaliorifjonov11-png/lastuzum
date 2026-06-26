from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    category = models.CharField(max_length=20)
    
    def __str__(self):
        return self.category

class Item(models.Model):
    category = models.ForeignKey("Category",  on_delete=models.CASCADE, null=True)
    rasm = models.ImageField(upload_to='media')
    narxi = models.IntegerField()
    skidkasi = models.IntegerField()
    tavsifi = models.CharField(max_length=100)

    def __str__(self):
        return self.tavsifi
    
class Men(models.Model ):
    category1 = models.ForeignKey("Category", on_delete=models.CASCADE, null=True)
    rasm1 = models.ImageField(upload_to='media')
    narxi1 = models.IntegerField()
    skidkasi1 = models.IntegerField()
    tavsifi1 = models.CharField(max_length=100)

    def __str__(self):
        return self.tavsifi1
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE
    )

    item = models.ForeignKey(
        Item,
        on_delete=models.CASCADE
    )

    quantity = models.PositiveIntegerField(default=1)
    
    
class Main_branch(models.Model):
    picture = models.ImageField(upload_to="media")
    desc = models.TextField(blank=True)

    def __str__(self):
        return self.desc
    
class Contact(models.Model):
    name = models.CharField(max_length=200)
    text = models.TextField()
    
# foreginKey ---- boshqa model