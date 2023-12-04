# Generated by Django 4.2.7 on 2023-12-04 15:41

import ckeditor.fields
import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='News_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
                ('summary', models.TextField()),
                ('content', models.TextField(blank=True, null=True)),
                ('image_thumb', models.ImageField(blank=True, upload_to='website/news_categories/')),
                ('image_description', models.CharField(blank=True, default='Imagem de noticia', max_length=75)),
                ('published', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='new_category', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
                ('summary', ckeditor.fields.RichTextField()),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('image_thumb', models.ImageField(blank=True, upload_to='website/news/')),
                ('image_description', models.CharField(blank=True, default='Imagem de noticia', max_length=75)),
                ('published', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='service', to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='new', to='website.news_category')),
            ],
        ),
        migrations.CreateModel(
            name='Frequent_Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('slug', models.SlugField()),
                ('answer', models.TextField()),
                ('published', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='frenquent_questions', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
