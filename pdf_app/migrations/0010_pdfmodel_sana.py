# Generated by Django 4.0.3 on 2022-05-07 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdf_app', '0009_pdfmodel_jinsi'),
    ]

    operations = [
        migrations.AddField(
            model_name='pdfmodel',
            name='sana',
            field=models.DateField(null=True),
        ),
    ]
