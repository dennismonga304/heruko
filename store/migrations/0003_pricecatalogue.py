# Generated by Django 2.2.14 on 2021-08-01 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_discription'),
    ]

    operations = [
        migrations.CreateModel(
            name='PriceCatalogue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('price_pack', models.FloatField()),
            ],
        ),
    ]
