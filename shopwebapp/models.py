from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone


stock_choose = [(True,'IN STOCK'),(False,'OUT OF STOCK')]



class Category(models.Model):
    Category_Name = models.CharField(max_length=50)
    category_created_date = models.DateTimeField(default=timezone.now(), blank=True)
    def __str__(self):
        return self.Category_Name



# Create your models here.
class Product(models.Model):
    Product_Image = models.ImageField(upload_to='uploads/')
    Name = models.CharField(max_length=100)
    Price = models.IntegerField()
    Discount_Price = models.IntegerField()
    Quantity = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(50)])
    In_Stock = models.CharField(max_length=20, choices = stock_choose, default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_created_date = models.DateTimeField(default=timezone.now(), blank=True)



