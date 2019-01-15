# Generated by Django 2.1 on 2019-01-15 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Addtime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('ctime', models.DateTimeField(auto_now=True)),
                ('uptime', models.DateTimeField(auto_now_add=True)),
                ('info', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': '日期及其他类型',
                'db_table': 'add_time',
            },
        ),
    ]