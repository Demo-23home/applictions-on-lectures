# Generated by Django 4.1 on 2022-08-29 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_remove_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='posts/'),
        ),
    ]
