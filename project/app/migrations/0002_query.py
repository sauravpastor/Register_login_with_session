# Generated by Django 5.0.6 on 2024-05-16 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.EmailField(max_length=50)),
                ('Title', models.CharField(max_length=100)),
                ('discription', models.TextField(max_length=100)),
            ],
        ),
    ]
