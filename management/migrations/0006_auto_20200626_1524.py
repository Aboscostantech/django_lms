# Generated by Django 3.0.4 on 2020-06-26 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0005_auto_20200626_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='show',
            field=models.BooleanField(default=False),
        ),
    ]