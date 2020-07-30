# Generated by Django 3.0.7 on 2020-07-30 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_users_email_verified'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='genderid',
            new_name='gender',
        ),
        migrations.RenameField(
            model_name='users',
            old_name='email_verified',
            new_name='is_active',
        ),
        migrations.RenameField(
            model_name='users',
            old_name='userid',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.EmailField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='login_method',
            field=models.CharField(choices=[('user', 'user'), ('kakao', 'Kakao'), ('kakao', 'google')], default='user', max_length=50),
        ),
        migrations.AlterField(
            model_name='users',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterModelTable(
            name='skintypes',
            table='_user_skintypes',
        ),
        migrations.AlterModelTable(
            name='skinworries',
            table='uesr_skinworries',
        ),
    ]