# Generated by Django 4.2.3 on 2023-07-09 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_cee', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='cee blogged', max_length=255),
        ),
    ]
