# Generated by Django 4.1.7 on 2023-04-08 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmyweb', '0009_grade_user_alter_actor_titles_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='additionalinfo',
            name='movie_type',
            field=models.PositiveSmallIntegerField(choices=[(4, 'Fantasy'), (0, 'Unknown'), (5, 'Action'), (2, 'Comedy'), (3, 'Sci-fi'), (1, 'Horror')], default=0),
        ),
    ]