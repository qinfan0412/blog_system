# Generated by Django 2.2.1 on 2019-09-28 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogindex', '0004_auto_20190928_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='description',
            field=models.TextField(),
        ),
    ]
