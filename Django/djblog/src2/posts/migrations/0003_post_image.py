# Generated by Django 4.1 on 2022-08-29 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='', upload_to='posts/'),
            preserve_default=False,
        ),
    ]
