# Generated by Django 4.0.3 on 2022-08-14 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='content',
            field=models.TextField(max_length=5000),
        ),
    ]