# Generated by Django 4.1.4 on 2022-12-30 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authtest', '0004_alter_subject_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('answer', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='subject',
            name='body',
        ),
    ]
