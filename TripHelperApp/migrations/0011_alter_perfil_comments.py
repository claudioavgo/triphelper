# Generated by Django 4.2.5 on 2023-10-31 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TripHelperApp', '0010_remove_comment_id_comment_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='comments',
            field=models.ManyToManyField(blank=True, default=None, to='TripHelperApp.comment'),
        ),
    ]
