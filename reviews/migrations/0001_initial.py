# Generated by Django 3.0.7 on 2020-07-26 18:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SkinType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'skintypes',
            },
        ),
        migrations.CreateModel(
            name='Worry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'worries',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True, null=True)),
                ('updated', models.DateField(auto_now=True, null=True)),
                ('star_point', models.IntegerField(default=0)),
                ('content', models.TextField(max_length=1000)),
                ('image_url', models.TextField(max_length=255)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Product')),
                ('skintype', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='reviews.SkinType')),
                ('worry', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='reviews.Worry')),
            ],
            options={
                'db_table': 'reviews',
            },
        ),
    ]
