# Generated by Django 4.0.3 on 2022-05-05 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PdfModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('surname', models.CharField(max_length=100, null=True)),
                ('kasb', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=100, null=True)),
                ('phone', models.CharField(max_length=100, null=True)),
                ('manzil', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
