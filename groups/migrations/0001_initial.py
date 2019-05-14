# Generated by Django 2.2.1 on 2019-05-14 08:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='groups_images/', verbose_name='img')),
                ('name', models.CharField(max_length=64)),
                ('description', models.CharField(blank=True, max_length=512)),
                ('parent_group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='groups.Group')),
            ],
        ),
    ]
