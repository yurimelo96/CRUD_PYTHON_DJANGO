# Generated by Django 4.1.3 on 2022-11-21 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0007_alter_transacao_valor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('bairro', models.CharField(max_length=200)),
                ('endereco', models.CharField(max_length=200)),
            ],
        ),
    ]
