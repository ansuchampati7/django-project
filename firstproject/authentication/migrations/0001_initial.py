# Generated by Django 3.2.8 on 2021-11-11 20:20

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('interface', '0002_alter_addusers_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='addblog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tittle', models.CharField(max_length=100)),
                ('post', models.TextField(max_length=1000)),
                ('date', models.DateTimeField(default=datetime.datetime(2021, 11, 12, 1, 50, 29, 641939))),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interface.addusers')),
            ],
        ),
    ]
