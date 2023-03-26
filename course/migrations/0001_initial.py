# Generated by Django 4.1.7 on 2023-03-26 07:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('config', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.CharField(max_length=200, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, max_length=1000, null=True, verbose_name='description')),
                ('img', models.ImageField(blank=True, upload_to='images/')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is active?')),
                ('foreign', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='foreign_courses', to='config.language', verbose_name='foreign')),
                ('native', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='native_courses', to='config.language', verbose_name='native')),
            ],
            options={
                'verbose_name': 'course',
                'verbose_name_plural': 'courses',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sequence', models.IntegerField(default=0, verbose_name='sequence')),
                ('name', models.CharField(default='Level', max_length=200, verbose_name='name')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('course', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='levels', to='course.course', verbose_name='course')),
            ],
            options={
                'verbose_name': 'level',
                'verbose_name_plural': 'levels',
                'ordering': ['sequence'],
            },
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=200, verbose_name='foreign')),
                ('description', models.CharField(default='', max_length=200, verbose_name='native')),
                ('literal_translation', models.CharField(blank=True, default='', max_length=200, null=True, verbose_name='literal translation')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is active')),
                ('media_type', models.CharField(blank=True, choices=[('AUDIO', 'Audio'), ('VIDEO', 'Video'), ('IMAGE', 'Image')], default=None, max_length=200, null=True)),
                ('path_to_file', models.FileField(blank=True, null=True, upload_to='word/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='words', to='course.course')),
                ('level', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='level_words', to='course.level')),
            ],
            options={
                'verbose_name': 'word',
                'verbose_name_plural': 'words',
                'ordering': ['level__sequence'],
            },
        ),
        migrations.CreateModel(
            name='WordMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media_type', models.CharField(choices=[('AUDIO', 'Audio'), ('VIDEO', 'Video'), ('IMAGE', 'Image')], default='IMAGE', max_length=200)),
                ('path_to_file', models.FileField(blank=True, upload_to='word/')),
                ('word', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medias', to='course.word')),
            ],
            options={
                'verbose_name': 'word media',
                'verbose_name_plural': 'word medias',
            },
        ),
        migrations.AddIndex(
            model_name='course',
            index=models.Index(fields=['name'], name='course_cour_name_7fe66a_idx'),
        ),
    ]
