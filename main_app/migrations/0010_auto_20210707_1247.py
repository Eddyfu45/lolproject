# Generated by Django 3.2.4 on 2021-07-07 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_alter_comment_champion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='champion',
            name='abilityDescriptionE',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='champion',
            name='abilityDescriptionQ',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='champion',
            name='abilityDescriptionR',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='champion',
            name='abilityDescriptionW',
            field=models.CharField(max_length=500),
        ),
    ]