# Generated by Django 2.2.5 on 2019-09-21 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0005_mainshow'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeid', models.IntegerField(default=1)),
                ('typename', models.CharField(max_length=32)),
                ('childtypenames', models.CharField(max_length=255)),
                ('typesort', models.IntegerField(default=1)),
            ],
            options={
                'db_table': 'axf_foodtype',
            },
        ),
    ]
