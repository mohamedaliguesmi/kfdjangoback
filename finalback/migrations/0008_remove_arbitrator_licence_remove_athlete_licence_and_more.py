# Generated by Django 4.1.1 on 2022-09-27 10:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finalback', '0007_remove_role_user_profile_role_alter_role_roles'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='arbitrator',
            name='licence',
        ),
        migrations.RemoveField(
            model_name='athlete',
            name='licence',
        ),
        migrations.RemoveField(
            model_name='coach',
            name='licence',
        ),
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='country',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='finalback.role'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='state',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='zip_code',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
