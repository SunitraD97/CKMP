# Generated by Django 2.1.3 on 2019-07-25 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20190725_1244'),
    ]

    operations = [
        migrations.AddField(
            model_name='chemistry',
            name='destroy',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='chemistry',
            name='density',
            field=models.FloatField(),
        ),
    ]
