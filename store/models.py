from django.db import models
from product.models import Product


class Slider(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='slider')
    title = models.CharField(max_length=250)

    def __str__(self):
        return f"slider - {self.product}"

class Banner(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='banner')
    description = models.CharField(max_length=250)

    def __str__(self):
        return f"banner - {self.product}"












