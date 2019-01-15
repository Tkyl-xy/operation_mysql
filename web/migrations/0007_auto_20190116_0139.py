# Generated by Django 2.1 on 2019-01-15 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_auto_20190116_0116'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
                ('sex', models.CharField(max_length=18)),
                ('email', models.EmailField(max_length=18)),
            ],
        ),
        migrations.CreateModel(
            name='UserGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=16)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='usergroup_user',
            field=models.ManyToManyField(to='web.UserGroup'),
        ),
    ]
