# Generated by Django 4.2.10 on 2024-03-19 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='admission_no',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]