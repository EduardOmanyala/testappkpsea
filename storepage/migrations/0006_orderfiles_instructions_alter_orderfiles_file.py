# Generated by Django 4.2.6 on 2024-01-23 00:01

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('storepage', '0005_orderfiles'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderfiles',
            name='instructions',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='orderfiles',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='order_doc/'),
        ),
    ]
