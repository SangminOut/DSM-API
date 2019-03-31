# Generated by Django 2.0.13 on 2019-03-31 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oauth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentmodel',
            name='name',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='studentmodel',
            name='number',
            field=models.IntegerField(null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='studentmodel',
            name='uuid',
            field=models.CharField(max_length=256, null=True, unique=True),
        ),
    ]
