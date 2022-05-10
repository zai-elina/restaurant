# Generated by Django 4.0.2 on 2022-05-09 15:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('order_list', '0004_alter_order_date_order_alter_orderitem_date_add'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['-date_order'], 'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Официант'),
        ),
        migrations.AlterField(
            model_name='order',
            name='table',
            field=models.IntegerField(default=0, verbose_name='Номер столика'),
        ),
    ]
