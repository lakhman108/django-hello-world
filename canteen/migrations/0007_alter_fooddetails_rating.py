# Generated by Django 4.1.3 on 2024-05-31 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('canteen', '0006_fooddetails_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fooddetails',
            name='rating',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
