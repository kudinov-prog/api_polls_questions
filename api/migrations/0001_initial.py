# Generated by Django 2.2.10 on 2021-02-22 18:21

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('finished', models.DateTimeField(blank=True)),
                ('description', models.TextField(max_length=4096)),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='votes_poll', to='api.Poll')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='votes_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=1024)),
                ('question_type', models.CharField(choices=[('TEXT', 'TEXT'), ('CHOICE', 'CHOICE'), ('MULTICHOICE', 'MULTICHOICE')], max_length=32)),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Poll')),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=256)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices_question', to='api.Question')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(blank=True, max_length=512, null=True)),
                ('choice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers_choice', to='api.Choice')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers_question', to='api.Question')),
                ('vote', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers_vote', to='api.Vote')),
            ],
        ),
    ]
