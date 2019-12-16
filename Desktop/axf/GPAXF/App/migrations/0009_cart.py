# Generated by Django 2.2.5 on 2019-09-22 21:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0008_axfuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_goods_num', models.IntegerField(default=1)),
                ('c_is_select', models.BooleanField(default=True)),
                ('c_goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.Goods')),
                ('c_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.AXFUser')),
            ],
            options={
                'db_table': 'axf_cart',
            },
        ),
    ]
