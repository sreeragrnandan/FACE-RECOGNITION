# Generated by Django 2.1.2 on 2019-03-01 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_contact_photos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='Photos',
            field=models.CharField(default='0000000', max_length=100),
        ),
    ]
