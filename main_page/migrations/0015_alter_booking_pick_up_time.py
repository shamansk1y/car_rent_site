# Generated by Django 4.2.7 on 2024-01-02 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0014_booking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='pick_up_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]