# Generated by Django 3.0.6 on 2020-06-14 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20200614_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='end_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='start_date',
            field=models.DateField(null=True),
        ),
    ]