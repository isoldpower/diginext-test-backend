# Generated by Django 4.2.13 on 2024-06-30 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entity', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='label',
            name='id',
            field=models.AutoField(editable=False, primary_key=True, serialize=False),
        ),
    ]
