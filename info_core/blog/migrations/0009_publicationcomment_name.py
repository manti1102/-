# Generated by Django 5.0.8 on 2024-08-09 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_rename_is_sugar_publication_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicationcomment',
            name='name',
            field=models.CharField(default=True, max_length=100),
        ),
    ]
