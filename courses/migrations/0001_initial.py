# Generated by Django 4.1.5 on 2023-01-28 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=100, null=True)),
                ('price', models.IntegerField()),
                ('discount', models.IntegerField(default=0)),
                ('active', models.BooleanField(default=False)),
                ('resource', models.FileField(upload_to='files/resource')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('thumbnail', models.ImageField(upload_to='files/thumbnail')),
                ('length', models.IntegerField()),
            ],
        ),
    ]
