# Generated by Django 4.0.3 on 2022-05-07 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdf_app', '0018_remove_pdfmodel_kasb'),
    ]

    operations = [
        migrations.AddField(
            model_name='pdfmodel',
            name='oxirgi_ish_joy_lavozimi',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='pdfmodel',
            name='oxirgi_ish_joy_nomi',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='pdfmodel',
            name='oxirgi_ish_joy_vaqti',
            field=models.CharField(max_length=100, null=True),
        ),
    ]