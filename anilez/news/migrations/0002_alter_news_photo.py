# Generated by Django 4.0.2 on 2022-03-26 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='photo',
            field=models.ImageField(upload_to='photo/%Y/%m'),
        ),
    ]
