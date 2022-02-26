import json
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from customer.models import Customer
from product.models import Product

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    ordered = models.BooleanField(default=False)
    accepted_ship = models.BooleanField(default=False)
    complete = models.BooleanField(default=False)


    def get_shipping_adress(self):
        return self.shipping_adress_set.get(order=self).zip_code

    def get_items(self):
        return self.order_item_set.all()

    def add_to_order(self, product_id, count=1):
        print('product soni:', count)
        product = Product.objects.get(pk=product_id)

        order_item, created = Order_Item.objects.get_or_create(product=product, order=self)
        if created == False:
            if order_item.quantity + count <= product.quantity:
                order_item.quantity += count
                order_item.save()
            else:
                order_item.quantity = product.quantity
                order_item.save()
        else:
            print('item yaratildi soni:', count)
            order_item.quantity = count
            order_item.save()


    def remove_from_order(self,product_id):
        product=Product.objects.get(pk=product_id)
        try:
            order_item=Order_Item.objects.get(product=product,order=self)

            if order_item.quantity == 1:
                print('item ga teng',order_item.quantity)
                order_item.delete(using=None,keep_parents=False)
            elif order_item.quantity > 1:
                print("order item 1 dan kup::",order_item.quantity)
                order_item.quantity -= 1
                order_item.save()


        except ObjectDoesNotExist:
            pass



    @property
    def get_total_price(self):
        orderitems = self.order_item_set.all()
        total = sum([item.get_total_price for item in orderitems])
        return total


    @property
    def get_cart_total(self):
        orderitems = self.order_item_set.all()
        total = sum([item.quantity for item in orderitems])
        return total



    def __str__(self):
        return f"{self.customer}-{self.id}"



class Order_Item(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    date_add = models.DateTimeField(auto_now_add=True)


    def get_product(self):
        return self.product

    @property
    def get_total_price(self):
        if self.product.quantity == 0:
            self.quantity = 0
            self.save()


        return self.product.price * self.quantity

    def __str__(self):
        return str("{} {}".format(self.product, self.quantity))



class Shipping_Adress(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,null=True)
    adress = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=50)
    date_add = models.DateTimeField(auto_now_add=True)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.adress


class Wishlist(models.Model):
    products = models.ManyToManyField(Product)
    customer = models.ForeignKey(Customer, null=True, blank=True, on_delete=models.SET_NULL)

    def get_total_product(self):
        return len(self.products.all())

    def get_selected(self, product):
        if product in self.products.all():
            return True
        return False

    def __str__(self):
        return f"wishlist - {self.customer}"