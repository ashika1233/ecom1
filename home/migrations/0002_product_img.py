# Generated by Django 5.0.7 on 2024-08-21 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='img',
            field=models.CharField(default='no image', max_length=200),
        ),
    ]
