# Generated by Django 3.2.15 on 2022-08-30 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_followerscount_likepost_post_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profileimg',
            field=models.ImageField(default='blank-profile-picture.png', upload_to='static/Profile/profile_images'),
        ),
    ]
