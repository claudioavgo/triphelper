# Generated by Django 4.2.5 on 2023-10-31 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TripHelperApp', '0012_remove_comment_uuid_comment_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.CharField(blank=True, default='Nenhum', null=True),
        ),
    ]
