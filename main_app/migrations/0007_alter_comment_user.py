# Generated by Django 3.2.4 on 2021-07-07 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_alter_comment_champion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.CharField(max_length=100),
        ),
    ]
