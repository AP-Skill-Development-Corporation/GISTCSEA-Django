# Generated by Django 3.0 on 2022-07-15 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rln', models.CharField(max_length=11)),
                ('sn', models.CharField(max_length=150)),
                ('brch', models.CharField(choices=[('DN', 'Select Your Branch'), ('CSE', 'Computer Science and Engineering'), ('MECH', 'Mechanical Engineering')], default='DN', max_length=5)),
                ('year', models.IntegerField(choices=[(0, 'Select Your Year'), (1, '1st Year'), (2, '2nd Year'), (3, '3rd Year'), (4, '4th Year')], default=0)),
            ],
        ),
    ]
