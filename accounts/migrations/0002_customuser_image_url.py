# Generated by Django 3.0.4 on 2020-03-27 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='image_url',
            field=models.TextField(default='https://i0.wp.com/aqyi.org/wp-content/uploads/2017/12/blank-profile.png?fit=449%2C449&ssl=1&w=640'),
        ),
    ]
