# Generated by Django 2.2.5 on 2019-10-17 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gdrive', '0003_auto_20191016_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='files',
            field=models.FileField(upload_to=''),
        ),
    ]
