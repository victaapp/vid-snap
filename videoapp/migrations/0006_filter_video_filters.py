# Generated by Django 4.2.3 on 2023-07-15 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videoapp', '0005_alter_subtitlefiles_subtitle_alter_video_video_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='Filter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='video',
            name='filters',
            field=models.ManyToManyField(to='videoapp.filter'),
        ),
    ]
