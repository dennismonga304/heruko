# Generated by Django 2.2.14 on 2021-08-04 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_delete_pricecatalogue'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customerscontact',
            old_name='fname',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='customerscontact',
            name='phonenumber',
        ),
        migrations.RemoveField(
            model_name='customerscontact',
            name='sname',
        ),
        migrations.RemoveField(
            model_name='customerscontact',
            name='tname',
        ),
    ]
