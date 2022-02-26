from product.models import Product, Category, Discount
from django.forms import ModelForm, Select, TextInput, NumberInput, Textarea, DateTimeInput, FileInput, SelectMultiple



class DiscountForm(ModelForm):
    class Meta:
        model = Discount
        fields = '__all__'


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'



class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


