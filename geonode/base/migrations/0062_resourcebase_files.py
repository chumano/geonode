# Generated by Django 3.2 on 2021-05-28 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0061_merge_0060_auto_20210512_1658_0060_resourcebase_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='resourcebase',
            name='files',
            field=models.JSONField(default=dict),
        ),
    ]
