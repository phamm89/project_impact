# Generated by Django 2.2.4 on 2019-08-12 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20190811_2211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='upload',
            field=models.FileField(default='core/static/default_avatar.png', upload_to=''),
        ),
    ]