# Generated by Django 2.1.7 on 2019-03-21 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='property',
            old_name='StartingBid',
            new_name='startingBid',
        ),
        migrations.AddField(
            model_name='property',
            name='cancelledBid',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='property',
            name='finalBid',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
