# Generated by Django 4.0.2 on 2022-04-04 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_mod', '0003_alter_platform_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='platform',
            name='description',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='platform',
            name='platform_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='project_table',
            name='documentation',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='project_table',
            name='project_name',
            field=models.CharField(max_length=100),
        ),
    ]