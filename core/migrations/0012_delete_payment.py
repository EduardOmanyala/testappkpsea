# Generated by Django 4.2 on 2023-08-25 11:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_alter_progress_category'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Payment',
        ),
    ]
