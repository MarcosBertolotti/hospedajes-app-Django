# Generated by Django 2.2.6 on 2019-11-07 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospedajes_app', '0013_auto_20191106_2037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/'),
        ),
    ]
