# Generated by Django 5.0.8 on 2024-08-12 12:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_alter_publicationcomment_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='publicationcomment',
            old_name='name',
            new_name='title',
        ),
    ]
