# Generated by Django 4.2.7 on 2023-11-28 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0010_contacts'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField(blank=True, max_length=250)),
                ('subject', models.CharField(max_length=50)),
                ('date', models.DateField(auto_now_add=True)),
                ('date_processing', models.DateField(auto_now=True)),
                ('is_processed', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': "Зворотній зв'язок",
                'ordering': ('-date',),
            },
        ),
    ]
