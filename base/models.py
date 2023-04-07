from django.db import models
from user.models import UserModel

class Product(models.Model):
    class Meta:
        db_table = "product"
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    code = models.CharField(max_length=5)
    name = models.CharField(max_length=20)
    type = models.CharField(max_length=200)
    price = models.FloatField(null=True, default=0)
    sizes = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('F', 'Free'),
    )
    size = models.CharField(choices=sizes, max_length=1)