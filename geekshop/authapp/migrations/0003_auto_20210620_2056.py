# Generated by Django 3.2.4 on 2021-06-20 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0002_auto_20210620_1859'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shopuser',
            name='activation_key_expires',
        ),
        migrations.AddField(
            model_name='shopuser',
            name='activation_key_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
