# Generated by Django 3.2.6 on 2023-02-19 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('degree', models.CharField(max_length=100)),
                ('experience', models.IntegerField()),
                ('specialization', models.CharField(max_length=100)),
                ('is_available', models.BooleanField(default=True)),
            ],
        ),
    ]
