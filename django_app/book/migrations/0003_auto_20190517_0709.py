# Generated by Django 2.2 on 2019-05-17 07:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20190514_1025'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['-created_at', '-updated_at']},
        ),
    ]
