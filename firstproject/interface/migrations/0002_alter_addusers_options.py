# Generated by Django 3.2.8 on 2021-11-11 20:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interface', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='addusers',
            options={'ordering': ['email']},
        ),
    ]
