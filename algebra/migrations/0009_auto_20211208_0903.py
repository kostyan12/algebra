# Generated by Django 3.2.9 on 2021-12-08 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('algebra', '0008_expressions_text_r'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='expressions',
            options={'ordering': ['-cr_date'], 'permissions': (('can_add_new_expr', 'Can add new expression'), ('can_add_new_eq', 'Can add new equation'))},
        ),
        migrations.AddField(
            model_name='expressions',
            name='cr_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
