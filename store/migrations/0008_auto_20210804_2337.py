# Generated by Django 2.2.14 on 2021-08-04 21:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_auto_20210804_1949'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customerscontact',
            old_name='mail',
            new_name='email',
        ),
    ]
