# Generated by Django 4.1.5 on 2023-01-28 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='slug',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
