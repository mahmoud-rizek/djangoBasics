# Generated by Django 4.0.3 on 2022-08-14 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_postmodel_name_alter_postmodel_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='img',
            field=models.ImageField(default=1, upload_to='posts/'),
            preserve_default=False,
        ),
    ]
