# Generated by Django 2.2.6 on 2019-10-30 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bebida_desejada', models.CharField(max_length=20)),
                ('marca_desejada', models.CharField(max_length=20)),
                ('quant_desejada', models.CharField(max_length=10)),
            ],
        ),
    ]