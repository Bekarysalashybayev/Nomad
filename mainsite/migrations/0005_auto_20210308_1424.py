# Generated by Django 2.2.10 on 2021-03-08 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0004_insurance'),
    ]

    operations = [
        migrations.AddField(
            model_name='insurance',
            name='doc1',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='insurance',
            name='doc2',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='insurance',
            name='doc3',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
