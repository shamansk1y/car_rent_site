# Generated by Django 4.2.7 on 2023-11-25 17:30

import blog.utils
import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True)),
                ('is_visible', models.BooleanField(default=True)),
                ('image', models.ImageField(upload_to=blog.utils.get_file_name_id)),
                ('position', models.IntegerField(default=0)),
                ('content', ckeditor.fields.RichTextField()),
                ('meta_title', models.CharField(blank=True, max_length=255, null=True)),
                ('meta_description', models.CharField(blank=True, max_length=255, null=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Блог',
                'ordering': ('-pub_date',),
            },
        ),
    ]
