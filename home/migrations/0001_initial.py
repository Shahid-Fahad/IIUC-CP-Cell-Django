# Generated by Django 4.0 on 2021-12-27 15:22

from django.db import migrations, models
import embed_video.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=255)),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('ps', models.IntegerField(default=0)),
                ('url', embed_video.fields.EmbedVideoField()),
                ('uploader', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['-added'],
            },
        ),
    ]
