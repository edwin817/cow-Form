# Generated by Django 3.2.1 on 2023-06-08 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cartdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.CharField(blank=True, max_length=30, null=True)),
                ('productqut', models.IntegerField(blank=True, null=True)),
                ('totalprice', models.IntegerField(blank=True, null=True)),
                ('productprice', models.IntegerField(blank=True, null=True)),
                ('user', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
    ]
