# Generated by Django 2.0.7 on 2019-07-25 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0013_auto_20190525_0805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]