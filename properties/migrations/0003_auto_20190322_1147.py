# Generated by Django 2.1.7 on 2019-03-22 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0002_auto_20190321_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='account',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='address',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='cancelledBid',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='city',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='finalBid',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='homeStead',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='landSF',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='legalDescription',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='livingSF',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='notes',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='ownerName',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='startingBid',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='state',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='subjectToNotIncludedInSale',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='taxesCoveredInSuit',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='totalTaxesOwed',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='valuesAdjudged',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='valuesBldgCAD',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='valuesCAD',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='valuesLandCAD',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='yearBuilt',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='zillowID',
            field=models.CharField(max_length=50, null=True),
        ),
    ]