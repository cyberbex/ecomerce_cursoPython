# Generated by Django 2.2.4 on 2024-03-19 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0008_auto_20240319_0628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='preco_marketing_promocional',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='variacao',
            name='preco_promocional',
            field=models.FloatField(default=0),
        ),
    ]
