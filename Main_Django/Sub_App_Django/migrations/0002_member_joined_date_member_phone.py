# Generated by Django 4.2.1 on 2023-06-05 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sub_App_Django', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='joined_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='phone',
            field=models.IntegerField(null=True),
        ),
    ]
