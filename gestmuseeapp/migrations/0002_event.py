# Generated by Django 4.1.3 on 2023-01-19 19:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestmuseeapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True, help_text='Nom de la Manifestation', null=True, verbose_name='Nom de la Manifestation')),
                ('theme', models.CharField(blank=True, max_length=30, null=True, verbose_name='Nom de la Manifestation')),
                ('start_day', models.DateField(default=datetime.date.today, help_text='Date de début de la Manifestation', verbose_name='Date de début de la Manifestation')),
                ('end_day', models.DateField(default=datetime.date.today, help_text='Date de fin de la Manifestation', verbose_name='Date de fin de la Manifestation')),
                ('start_time', models.TimeField(help_text='Starting time', verbose_name='Starting time')),
                ('end_time', models.TimeField(help_text='Final time', verbose_name='Final time')),
                ('image', models.ImageField(default='static/img/manifestations/next.png', upload_to='static/img/manifestations')),
                ('notes', models.TextField(blank=True, help_text='Résumé', null=True, verbose_name='Résumé')),
            ],
            options={
                'verbose_name': 'Manifestations',
                'verbose_name_plural': 'Manifestations',
            },
        ),
    ]
