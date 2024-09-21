import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='A label for name tag.', max_length=31, unique=True)),
                ('slug', models.SlugField(help_text='A label for URL config.', max_length=31, unique=True)),
            ],
            options={
                'verbose_name': 'Tag',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='Назва поста')),
                ('body', models.TextField()),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('DF', 'Draft'), ('PB', 'Published')], default='DF', max_length=2)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='blog.category')),
                ('tags', models.ManyToManyField(related_name='blog_posts', to='blog.tag')),
            ],
            options={
                'verbose_name': 'Публікація',
                'verbose_name_plural': 'Публікації',
                'ordering': ['-publish'],
            },
        ),
    ]