# Generated by Django 4.0.3 on 2022-05-07 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdf_app', '0015_remove_pdfmodel_work_experience_alter_pdfmodel_oylik'),
    ]

    operations = [
        migrations.AddField(
            model_name='pdfmodel',
            name='prava',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
