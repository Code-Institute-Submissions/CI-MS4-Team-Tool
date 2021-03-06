# Generated by Django 3.0.6 on 2020-06-24 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AgentRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_name', models.CharField(max_length=64)),
                ('role_color', models.CharField(max_length=6)),
                ('company_id', models.CharField(editable=False, max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_id', models.CharField(editable=False, max_length=32)),
                ('shift_name', models.CharField(max_length=64)),
                ('shift_start', models.TimeField()),
                ('shift_end', models.TimeField()),
                ('min_agents', models.IntegerField(default=1)),
                ('weekday_sunday', models.BooleanField(default=True)),
                ('weekday_monday', models.BooleanField(default=True)),
                ('weekday_tuesday', models.BooleanField(default=True)),
                ('weekday_wednesday', models.BooleanField(default=True)),
                ('weekday_thursday', models.BooleanField(default=True)),
                ('weekday_friday', models.BooleanField(default=True)),
                ('weekday_saturday', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_id', models.CharField(editable=False, max_length=32)),
                ('team_name', models.CharField(default='Teamname', max_length=64)),
                ('planning_deadline', models.IntegerField(default=0)),
                ('coaching_rep', models.IntegerField(default=0)),
                ('min_lunchbreak', models.IntegerField(default=30)),
                ('min_dinnerbreak', models.IntegerField(default=30)),
                ('min_paidbreak', models.IntegerField(default=15)),
            ],
        ),
    ]
