# Generated by Django 4.2.7 on 2023-11-18 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cadastral_number', models.IntegerField()),
                ('width', models.IntegerField()),
                ('longitude', models.IntegerField()),
                ('status', models.BooleanField()),
            ],
        ),
    ]
