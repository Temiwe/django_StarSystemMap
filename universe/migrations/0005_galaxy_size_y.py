# Generated by Django 3.2.3 on 2021-07-25 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universe', '0004_alter_galaxy_size_x'),
    ]

    operations = [
        migrations.AddField(
            model_name='galaxy',
            name='size_y',
            field=models.IntegerField(null=True),
        ),
    ]
