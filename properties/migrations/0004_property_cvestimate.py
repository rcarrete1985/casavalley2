# Generated by Django 2.1.7 on 2019-03-22 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0003_auto_20190322_1147'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='cvEstimate',
            field=models.IntegerField(null=True),
        ),
    ]
