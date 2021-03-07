# Generated by Django 2.2.10 on 2021-03-07 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('img', models.ImageField(blank=True, null=True, upload_to='images')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]