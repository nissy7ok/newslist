# Generated by Django 3.1 on 2020-08-23 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newslistapp', '0005_auto_20200822_2120'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='icon',
            field=models.CharField(default=20200823, max_length=10),
            preserve_default=False,
        ),
    ]
