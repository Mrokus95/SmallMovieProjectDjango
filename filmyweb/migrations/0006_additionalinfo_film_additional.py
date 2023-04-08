# Generated by Django 4.1.7 on 2023-04-07 20:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('filmyweb', '0005_alter_film_director_alter_film_poster_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdditionalInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.PositiveSmallIntegerField(default=0)),
                ('watched', models.BooleanField(default=False)),
                ('movie_type', models.PositiveSmallIntegerField(choices=[(4, 'Fantasy'), (5, 'Action'), (3, 'Sci-fi'), (1, 'Horror'), (0, 'Unknown'), (2, 'Comedy')], default=0)),
            ],
        ),
        migrations.AddField(
            model_name='film',
            name='additional',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='filmyweb.additionalinfo'),
        ),
    ]