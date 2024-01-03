# Generated by Django 4.2.7 on 2023-11-28 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0008_car_airconditions_car_audio_car_bluetooth_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experienced', models.DecimalField(decimal_places=0, max_digits=10, verbose_name='Років роботи')),
                ('total_cars', models.DecimalField(decimal_places=0, max_digits=10, verbose_name='Кількість авто')),
                ('happy_costomers', models.DecimalField(decimal_places=0, max_digits=10, verbose_name='Задоволених клієнтів')),
                ('total_mileage', models.DecimalField(decimal_places=0, max_digits=10, verbose_name='Загальний пробіг')),
            ],
            options={
                'verbose_name_plural': 'Наш досвід',
                'ordering': ('experienced',),
            },
        ),
    ]