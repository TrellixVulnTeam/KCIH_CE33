# Generated by Django 2.2.3 on 2019-10-10 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Kisumu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='leader',
            name='is_leader',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='mca',
            name='is_mca',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='ministryofficial',
            name='is_ministry_off',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='mp',
            name='is_mp',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='unionofficial',
            name='is_union_off',
            field=models.BooleanField(default=True),
        ),
    ]
