# Generated by Django 3.0.1 on 2022-01-31 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_checkresume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='cv',
            field=models.FileField(upload_to='images'),
        ),
    ]
