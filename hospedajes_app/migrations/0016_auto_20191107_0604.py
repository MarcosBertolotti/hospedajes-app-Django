# Generated by Django 2.2.6 on 2019-11-07 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospedajes_app', '0015_auto_20191107_0555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
