# Generated by Django 2.2.1 on 2019-05-14 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('elements', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='element',
            name='parent_group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='elements', to='groups.Group'),
        ),
    ]