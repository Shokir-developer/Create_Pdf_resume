# Generated by Django 4.0.3 on 2022-05-07 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdf_app', '0008_rename_summary_pdfmodel_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='pdfmodel',
            name='jinsi',
            field=models.CharField(choices=[('erkak', 'erkak'), ('ayol', 'ayol')], max_length=100, null=True),
        ),
    ]
