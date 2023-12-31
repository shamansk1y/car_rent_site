# Generated by Django 4.2.7 on 2023-11-23 22:21

from django.db import migrations, models
import main_page.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hiro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Назва слайду')),
                ('position', models.SmallIntegerField(unique=True, verbose_name='Позиція')),
                ('back_image', models.ImageField(upload_to=main_page.utils.get_file_name, verbose_name='Фонове зображення')),
                ('is_visible', models.BooleanField(default=True, verbose_name='Видимість')),
                ('h_1', models.CharField(blank=True, max_length=250, verbose_name='Заголовок')),
                ('desc', models.TextField(blank=True, max_length=500, verbose_name='Опис')),
            ],
            options={
                'verbose_name_plural': 'Слайдер',
                'ordering': ('position',),
            },
        ),
    ]
