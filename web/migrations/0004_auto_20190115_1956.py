# Generated by Django 2.1 on 2019-01-15 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20190115_1942'),
    ]

    operations = [
        migrations.AddField(
            model_name='addtime',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='addtime',
            name='ip',
            field=models.GenericIPAddressField(blank=True, null=True, protocol='ipv4'),
        ),
    ]