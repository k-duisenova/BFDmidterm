# Generated by Django 3.1.7 on 2021-03-20 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.SmallIntegerField(choices=[(1, 'super admin'), (2, 'guest')], default=2),
        ),
    ]
