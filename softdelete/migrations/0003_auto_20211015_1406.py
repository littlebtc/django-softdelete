# Generated by Django 3.2 on 2021-10-15 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('softdelete', '0002_auto_20170912_0537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='changeset',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='softdeleterecord',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
