# Generated by Django 3.0.4 on 2020-03-27 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_article_edited'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='edited',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
