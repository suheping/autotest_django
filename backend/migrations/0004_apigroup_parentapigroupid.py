# Generated by Django 2.2.7 on 2020-03-26 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_remove_apigroup_parentapigroupid'),
    ]

    operations = [
        migrations.AddField(
            model_name='apigroup',
            name='parentApiGroupId',
            field=models.IntegerField(null=True, verbose_name='接口父分组id'),
        ),
    ]
