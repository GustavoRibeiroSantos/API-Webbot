# Generated by Django 2.2.6 on 2019-10-30 15:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0004_auto_20191030_1220'),
    ]

    operations = [
        migrations.RenameField(
            model_name='Model',
            old_name='marca_desejada',
            new_name='marca',
        ),
        migrations.RenameField(
            model_name='Model',
            old_name='quant_desejada',
            new_name='quant',
        ),
    ]