# Generated by Django 4.2.7 on 2023-11-27 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reserve',
            options={'verbose_name_plural': 'ثبت نام'},
        ),
        migrations.AlterField(
            model_name='reserve',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='ایمیل'),
        ),
        migrations.AlterField(
            model_name='reserve',
            name='number',
            field=models.PositiveIntegerField(max_length=20, verbose_name='تعداد'),
        ),
    ]
