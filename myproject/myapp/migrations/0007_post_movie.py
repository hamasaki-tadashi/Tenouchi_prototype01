# Generated by Django 3.2.9 on 2021-11-15 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_post_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='movie',
            field=models.FileField(blank=True, upload_to='image/'),
        ),
    ]
