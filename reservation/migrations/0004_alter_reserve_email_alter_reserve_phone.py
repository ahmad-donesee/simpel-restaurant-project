# Generated by Django 4.2.7 on 2023-11-27 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0003_alter_reserve_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserve',
            name='email',
            field=models.EmailField(max_length=40, verbose_name='ایمیل'),
        ),
        migrations.AlterField(
            model_name='reserve',
            name='phone',
            field=models.IntegerField(max_length=20, verbose_name='شماره تلفن'),
        ),
    ]
