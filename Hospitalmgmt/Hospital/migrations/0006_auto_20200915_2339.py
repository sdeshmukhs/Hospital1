# Generated by Django 3.0.2 on 2020-09-15 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hospital', '0005_itself'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itself',
            name='x',
            field=models.CharField(max_length=20),
        ),
    ]
