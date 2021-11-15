# Generated by Django 3.2.7 on 2021-11-15 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=150, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('current_money', models.FloatField(verbose_name='amount of initial money')),
                ('current_money_unit', models.CharField(max_length=10)),
            ],
        ),
    ]
