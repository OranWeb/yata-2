# Generated by Django 2.0.5 on 2019-04-14 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chain', '0028_attacks'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attacks',
            old_name='faction',
            new_name='report',
        ),
    ]