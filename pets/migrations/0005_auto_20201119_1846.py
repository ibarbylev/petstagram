# Generated by Django 3.1.3 on 2020-11-19 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0004_like_test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='image_url',
            field=models.ImageField(upload_to='images'),
        ),
    ]
