# Generated by Django 2.2.1 on 2019-09-28 10:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blogindex', '0005_auto_20190928_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='日期'),
        ),
    ]
