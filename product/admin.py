from django.contrib import admin
from .models import *
from django.forms import ModelChoiceField


class CategoryAdmin_Smartphone(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            category_all = Category.objects.all()
            parent_id_list = []
            category_list = []
            smartphone_category = Category.objects.filter(tree_id=Category.objects.get(name='Smartphone').tree_id)
            for i in smartphone_category:
                parent_id_list.append(i.parent_id)

            for a in smartphone_category:
                if a.id not in parent_id_list:
                    category_list.append(a.id)


            return ModelChoiceField(Category.objects.filter(id__in = category_list ))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class CategoryAdmin_Notebook(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            category_all = Category.objects.all()
            parent_id_list = []
            category_list = []
            notebook_category = Category.objects.filter(tree_id=Category.objects.get(name='Notebook').tree_id)
            for i in notebook_category:
                parent_id_list.append(i.parent_id)

            for a in notebook_category:
                if a.id not in parent_id_list:
                    category_list.append(a.id)


            return ModelChoiceField(Category.objects.filter(id__in = category_list ))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class DiscountAdmin(admin.ModelAdmin):
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        print(db_field)
        if db_field.name == "products":
            kwargs["queryset"] = Product.objects.filter(discount=None)
        return super(DiscountAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Category)
admin.site.register(Smartphone,CategoryAdmin_Smartphone)
admin.site.register(Notebook,CategoryAdmin_Notebook)
admin.site.register(Discount,DiscountAdmin)
admin.site.register(Comment)