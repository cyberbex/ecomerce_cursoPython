# Generated by Django 2.2.4 on 2024-03-19 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0005_auto_20240319_0610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='preco_marketing_promocional',
            field=models.FloatField(blank=True, verbose_name='Preço Promo.'),
        ),
    ]
