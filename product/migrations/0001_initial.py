# Generated by Django 3.2.5 on 2021-09-08 14:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('quantity', models.PositiveBigIntegerField(default=1)),
                ('description', models.CharField(max_length=500)),
                ('price', models.FloatField()),
                ('img', models.ImageField(upload_to='product')),
                ('date', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.category')),
            ],
        ),
        migrations.CreateModel(
            name='Notebook',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='product.product')),
                ('cpu', models.CharField(max_length=25, verbose_name='Processor')),
                ('dioganal', models.FloatField()),
                ('hdd_memory', models.IntegerField(help_text='Size - GB')),
                ('ssd_memory', models.IntegerField()),
                ('ram', models.IntegerField(help_text='Size - GB')),
                ('video_card', models.CharField(choices=[('integred', 'integred'), ('2', '2'), ('4', '4')], max_length=20)),
                ('camera', models.FloatField(help_text='size MP')),
                ('weight', models.FloatField(help_text='size - kg')),
            ],
            bases=('product.product',),
        ),
        migrations.CreateModel(
            name='Smartphone',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='product.product')),
                ('dioganal', models.FloatField(blank=True, null=True)),
                ('accumulator', models.IntegerField(blank=True, help_text='Battery power (mA*s)', null=True)),
                ('memory', models.IntegerField()),
                ('ram', models.IntegerField()),
                ('main_camera', models.IntegerField(help_text='Main Camer - (MP)')),
                ('front_camera', models.IntegerField(blank=True, help_text='MP', null=True)),
                ('finger_scanner', models.BooleanField(default=True)),
                ('nfc', models.BooleanField(default=True)),
            ],
            bases=('product.product',),
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percent', models.PositiveIntegerField()),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('products', models.ManyToManyField(to='product.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.CharField(max_length=250)),
                ('rating', models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=1)),
                ('date', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
