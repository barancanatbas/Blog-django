# Generated by Django 3.1.1 on 2020-10-18 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0011_auto_20201017_2304'),
    ]

    operations = [
        migrations.AddField(
            model_name='reports',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='gönderme tarihi'),
        ),
    ]