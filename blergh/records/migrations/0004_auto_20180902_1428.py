# Generated by Django 2.1.1 on 2018-09-02 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0003_auto_20180902_0831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edible',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]