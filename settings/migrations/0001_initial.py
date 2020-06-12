# Generated by Django 3.0.6 on 2020-06-12 22:39

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AgentRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_name', models.CharField(max_length=80)),
                ('role_color', models.IntegerField()),
            ],
        ),
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
                ('plan', models.CharField(blank=True, max_length=40, null=True)),
                ('signup_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('renewal_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('payment', models.DecimalField(decimal_places=0, default=0, max_digits=2)),
                ('setting_weekstart', models.DecimalField(decimal_places=0, default=0, max_digits=1)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(default='Teamname', max_length=64)),
                ('planning_deadline', models.IntegerField(default=0)),
                ('coaching_rep', models.IntegerField(default=0)),
                ('min_lunchbreak', models.IntegerField(default=30)),
                ('min_dinnerbreak', models.IntegerField(default=30)),
                ('min_paidbreak', models.IntegerField(default=15)),
            ],
        ),
    ]
