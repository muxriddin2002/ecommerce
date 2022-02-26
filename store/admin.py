from django.contrib import admin
from django.forms import ModelChoiceField
from .models import Banner,Slider
from product.models import Product

class SliderAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'product':
            return ModelChoiceField(Product.objects.filter(discount = not None))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)



admin.site.register(Slider,SliderAdmin)
admin.site.register(Banner)
