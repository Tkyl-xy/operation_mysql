# Generated by Django 2.1 on 2019-01-15 18:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_auto_20190116_0139'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='User2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
                ('sex', models.CharField(max_length=16)),
                ('email', models.EmailField(max_length=16)),
            ],
        ),
        migrations.AddField(
            model_name='admin',
            name='admin_user2',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='web.User2'),
        ),
    ]
