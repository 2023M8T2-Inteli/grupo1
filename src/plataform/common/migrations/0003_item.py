# Generated by Django 4.2.7 on 2023-12-19 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_authorizednumber'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=100)),
                ('x', models.IntegerField()),
                ('y', models.IntegerField()),
                ('z', models.IntegerField(default=0)),
            ],
        ),
    ]
