# Generated by Django 5.1.1 on 2024-09-09 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cheesecake',
            name='price',
            field=models.IntegerField(),
        ),
    ]
