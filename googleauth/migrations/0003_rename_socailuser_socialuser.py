# Generated by Django 4.1.1 on 2022-11-02 23:29

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("googleauth", "0002_socailuser"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="SocailUser",
            new_name="SocialUser",
        ),
    ]
