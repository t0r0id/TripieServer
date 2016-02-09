# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-09 14:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('signup', '0001_initial'),
        ('Plan', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Itinerary',
            fields=[
                ('ItineraryId', models.AutoField(default=0, primary_key=True, serialize=False)),
                ('CreatedOn', models.TimeField(default='09:00:00')),
                ('Visited', models.CharField(max_length=200)),
                ('ActiveItinerary', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ItineraryDestination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StartTime', models.TimeField(default='09:00:00')),
                ('Duration', models.DurationField(default='00:30:00')),
            ],
        ),
        migrations.CreateModel(
            name='ItineraryInput',
            fields=[
                ('ItineraryInputId', models.AutoField(default=0, primary_key=True, serialize=False)),
                ('ItineraryName', models.CharField(max_length=20)),
                ('StartTime', models.TimeField(default='09:00:00')),
                ('EndTime', models.TimeField(default='17:00:00')),
                ('StartLatitude', models.DecimalField(decimal_places=7, max_digits=10)),
                ('StartLongitude', models.DecimalField(decimal_places=7, max_digits=10)),
                ('EndLatitude', models.DecimalField(decimal_places=7, max_digits=10)),
                ('EndLongitude', models.DecimalField(decimal_places=7, max_digits=10)),
                ('Tags', models.CharField(max_length=200)),
                ('UserId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='signup.User')),
            ],
        ),
        migrations.CreateModel(
            name='ItineraryRoute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StartTime', models.TimeField(default='09:00:00')),
                ('Duration', models.DurationField(default='00:30:00')),
                ('ItineraryId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='itinerary.ItineraryInput')),
                ('RouteId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Plan.MumbaiLocation')),
            ],
        ),
        migrations.AddField(
            model_name='itinerarydestination',
            name='ItineraryId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='itinerary.ItineraryInput'),
        ),
        migrations.AddField(
            model_name='itinerarydestination',
            name='LocationId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Plan.MumbaiLocation'),
        ),
        migrations.AddField(
            model_name='itinerary',
            name='ItineraryInputId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='itinerary.ItineraryInput'),
        ),
    ]
