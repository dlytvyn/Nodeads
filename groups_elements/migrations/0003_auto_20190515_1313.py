# Generated by Django 2.2.1 on 2019-05-15 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups_elements', '0002_auto_20190515_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='element',
            name='description',
            field=models.TextField(blank=True, max_length=512),
        ),
        migrations.AlterField(
            model_name='group',
            name='description',
            field=models.TextField(blank=True, max_length=512),
        ),
    ]