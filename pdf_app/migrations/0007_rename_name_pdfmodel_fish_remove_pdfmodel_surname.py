# Generated by Django 4.0.3 on 2022-05-06 04:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pdf_app', '0006_rename_info_pdfmodel_summary_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pdfmodel',
            old_name='name',
            new_name='fish',
        ),
        migrations.RemoveField(
            model_name='pdfmodel',
            name='surname',
        ),
    ]
