# Generated by Django 4.2.7 on 2023-11-21 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=250)),
                ('occupation', models.CharField(max_length=250)),
                ('status', models.CharField(max_length=250)),
            ],
        ),
    ]
