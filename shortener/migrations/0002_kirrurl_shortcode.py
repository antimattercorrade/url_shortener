# Generated by Django 3.0.6 on 2020-05-09 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='kirrurl',
            name='shortcode',
            field=models.CharField(default='defaultshortcode', max_length=15),
            preserve_default=False,
        ),
    ]
