# Generated by Django 3.0.8 on 2020-07-09 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0052_auto_20200629_1553'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stocks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.IntegerField(default=0)),
                ('rackets', models.TextField(default='{}')),
            ],
        ),
    ]