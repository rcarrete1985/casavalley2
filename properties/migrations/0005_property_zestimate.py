# Generated by Django 2.1.7 on 2019-03-22 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0004_property_cvestimate'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='zestimate',
            field=models.IntegerField(null=True),
        ),
    ]
