# Generated by Django 4.2.5 on 2023-10-10 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_signin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Join',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Namej', models.CharField(max_length=50)),
                ('Bdatej', models.CharField(max_length=200)),
                ('Instaj', models.CharField(max_length=50)),
                ('Numberj', models.CharField(max_length=200)),
                ('Emailj', models.CharField(max_length=200)),
            ],
        ),
    ]