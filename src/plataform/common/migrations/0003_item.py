# Generated by Django 4.2.7 on 2023-12-20 15:59

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
                ('x', models.FloatField()),
                ('y', models.FloatField()),
                ('z', models.FloatField(default=0.0)),
                ('image_url', models.CharField(max_length=256)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
