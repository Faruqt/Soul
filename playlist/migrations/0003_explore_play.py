# Generated by Django 3.2.5 on 2021-08-04 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playlist', '0002_alter_explore_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='explore',
            name='play',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]