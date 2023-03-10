# Generated by Django 4.1.5 on 2023-01-29 06:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=200)),
                ('image', models.ImageField(upload_to='static/images')),
                ('content', models.TextField()),
                ('published', models.BooleanField(default=False)),
                ('tags', models.CharField(max_length=20)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.IntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='News.category')),
            ],
        ),
    ]
