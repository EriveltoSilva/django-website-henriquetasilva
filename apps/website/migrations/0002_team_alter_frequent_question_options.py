# Generated by Django 4.2.7 on 2023-12-04 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('function', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='website/team/')),
                ('image_description', models.CharField(default='', max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='frequent_question',
            options={'ordering': ['id', '-created_at']},
        ),
    ]
