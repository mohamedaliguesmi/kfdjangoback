# Generated by Django 4.1.1 on 2022-10-03 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finalback', '0013_alter_licences_activated_alter_seasons_seasons_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorie',
            name='categorie_age',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='grade',
            name='Grade',
            field=models.CharField(max_length=200),
        ),
    ]
