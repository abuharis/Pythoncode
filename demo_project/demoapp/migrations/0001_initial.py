# Generated by Django 5.0.2 on 2024-02-28 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('id', models.CharField(max_length=200, primary_key=True, serialize=False)),
            ],
        ),
    ]