# Generated by Django 5.0.2 on 2024-02-17 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentors',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
