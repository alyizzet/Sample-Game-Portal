# Generated by Django 3.0.8 on 2020-07-22 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_auto_20200706_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='image',
            field=models.ImageField(blank=True, upload_to='static/'),
        ),
    ]
