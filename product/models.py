import datetime
import sys
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import models
from mptt.models import TreeForeignKey,MPTTModel
from customer.models import Customer
import json
from PIL import Image



class Category(MPTTModel):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    def get_parent(self):
        return Category.objects.filter(parent_id=self.id)

    def __str__(self):
        return self.name




class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    quantity = models.PositiveBigIntegerField(default=1)
    description = models.CharField(max_length=500)
    price = models.FloatField()
    img = models.ImageField(upload_to='product')
    date = models.DateTimeField(auto_now=True)



    def get_info(self):
        info = {'name': self.name, 'price': self.price, 'image': self.img.url, 'description': self.description, 'product_id': self.id}
        info = json.dumps(info)
        return info



    def get_discount_endTime(self):
        discout = Discount.objects.get(products=self)
        end_time = discout.end_time
        return str(end_time)

    def get_discount(self):
        return self.discount_set.get(products=self).percent

    def get_price_discount(self):
        return self.price * (1 - ( self.get_discount() / 100 ))

    def get_comment(self):
        return self.comment_set.all()

    MIN_RESOLUTION = (400, 400)
    MAX_RESOLUTION = (650, 650)
    MAX_SIZE = 3145728

    def save(self, *args, **kwargs):
        image = self.img
        img = Image.open(image)
        new_image = img.convert("RGB")

        max_width, max_height = self.MAX_RESOLUTION
        min_width, min_height = self.MIN_RESOLUTION


        if img.height > max_height:

            height = img.height/max_height
        else:
            height = 1


        resized_new_image = new_image.resize((int(img.width/height), int(img.height/height)), Image.ANTIALIAS)

        filestream = BytesIO()
        resized_new_image.save(filestream, 'jpeg', quality=98)
        filestream.seek(0)
        name = '{}.{}'.format(*self.img.name.split('.'))
        print('name: ', name)
        self.img = InMemoryUploadedFile(
            filestream, 'ImageField', name, 'jpeg/image', sys.getsizeof(filestream), None
        )

        super().save(*args, **kwargs)



    def __str__(self):
        return self.name




class Smartphone(Product):
    dioganal = models.FloatField(blank=True,null=True)
    accumulator = models.IntegerField(blank=True,null=True,help_text='Battery power (mA*s)')
    memory = models.IntegerField()
    ram = models.IntegerField()
    main_camera = models.IntegerField(help_text='Main Camer - (MP)')
    front_camera = models.IntegerField(help_text='MP',blank=True,null=True)
    finger_scanner = models.BooleanField(default=True)
    nfc = models.BooleanField(default=True)


class Notebook(Product):
    Vedio_card = (
        ('integred', 'integred'),
        ('2', '2'),
        ('4', '4')
    )
    cpu = models.CharField(max_length=25,verbose_name='Processor')
    dioganal = models.FloatField()
    hdd_memory = models.IntegerField(help_text='Size - GB')
    ssd_memory = models.IntegerField()
    ram = models.IntegerField(help_text='Size - GB')
    video_card = models.CharField(max_length=20 ,choices=Vedio_card)
    camera = models.FloatField(help_text='size MP')
    weight = models.FloatField(help_text='size - kg')






class Comment(models.Model):
    RATING =(
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )
    user = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    review = models.CharField(max_length=250)
    rating = models.PositiveIntegerField(default=1,choices=RATING)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user} - {self.review[:15]}"




class Discount(models.Model):
    percent = models.PositiveIntegerField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    products = models.ManyToManyField(Product)

    def __str__(self):
        return f"{self.percent}%"



