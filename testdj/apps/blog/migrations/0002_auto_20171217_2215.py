# Generated by Django 2.0 on 2017-12-17 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='birthday',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='city',
            field=models.CharField(max_length=130, null=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='country',
            field=models.CharField(max_length=130, null=True),
        ),
    ]