# Generated by Django 4.1.3 on 2022-11-19 03:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0005_transacao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transacao',
            name='data',
        ),
    ]
