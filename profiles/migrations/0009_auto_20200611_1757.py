# Generated by Django 3.0.6 on 2020-06-11 17:57

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0008_remove_userprofile_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(blank=True, max_length=80, null=True)),
                ('street_address1', models.CharField(blank=True, max_length=80, null=True)),
                ('street_address2', models.CharField(blank=True, max_length=80, null=True)),
                ('country', django_countries.fields.CountryField(blank=True, max_length=2, null=True)),
                ('postcode', models.CharField(blank=True, max_length=20, null=True)),
                ('town_or_city', models.CharField(blank=True, max_length=40, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('plan', models.CharField(blank=True, max_length=40, null=True)),
                ('signup_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('renewal_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('payment', models.DecimalField(decimal_places=0, default=0, max_digits=2)),
            ],
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='company_name',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='country',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='payment',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='plan',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='postcode',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='renewal_date',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='signup_date',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='street_address1',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='street_address2',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='town_or_city',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='agent_goal',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='birthday_ddmm',
            field=models.CharField(default='0000', max_length=16),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='contract_percentage',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=3),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='contract_type',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='end_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='level',
            field=models.CharField(default='admin', max_length=16),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='role',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='start_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='team',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
    ]
