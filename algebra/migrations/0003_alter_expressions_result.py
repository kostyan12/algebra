# Generated by Django 3.2.9 on 2021-12-03 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('algebra', '0002_auto_20211201_1818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expressions',
            name='result',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
