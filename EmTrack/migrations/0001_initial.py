# Generated by Django 2.2.1 on 2020-01-28 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('job_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('job_title', models.CharField(max_length=35)),
                ('min_salary', models.IntegerField(blank=True, null=True)),
                ('max_salary', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'jobs',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employee_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(blank=True, max_length=20)),
                ('last_name', models.CharField(max_length=25)),
                ('email', models.CharField(max_length=25, unique=True)),
                ('phone_number', models.CharField(blank=True, max_length=20)),
                ('hire_date', models.DateField()),
                ('salary', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('commission_pct', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('department_id', models.IntegerField(blank=True, null=True)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='EmTrack.Job')),
                ('manager', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='EmTrack.Employee')),
            ],
            options={
                'db_table': 'employees',
            },
        ),
        migrations.CreateModel(
            name='JobHistory',
            fields=[
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, primary_key=True, serialize=False, to='EmTrack.Employee')),
                ('start_date', models.DateField(unique=True)),
                ('end_date', models.DateField()),
                ('department_id', models.IntegerField(blank=True, null=True)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='EmTrack.Job')),
            ],
            options={
                'db_table': 'job_history',
            },
        ),
    ]
