# Generated by Django 3.2 on 2021-04-22 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210422_0928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskitem',
            name='description',
            field=models.TextField(blank=True, max_length=600),
        ),
        migrations.AlterField(
            model_name='taskitem',
            name='title',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
