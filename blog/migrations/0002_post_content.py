# Generated by Django 3.0.5 on 2020-05-03 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=models.TextField(default='<Enter Your Content Here>', verbose_name='<Enter Your Content Here>'),
            preserve_default=False,
        ),
    ]
