# Generated by Django 2.1b1 on 2018-09-26 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='album',
            field=models.ForeignKey(on_delete='CASCADE', to='photo.Album'),
        ),
    ]
