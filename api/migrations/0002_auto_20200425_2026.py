# Generated by Django 3.0.5 on 2020-04-25 17:26

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ('id',)},
        ),
        migrations.AlterModelOptions(
            name='articlelike',
            options={'ordering': ('id',)},
        ),
    ]