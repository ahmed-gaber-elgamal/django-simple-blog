# Generated by Django 3.0 on 2020-12-19 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simple_blog', '0007_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
    ]
