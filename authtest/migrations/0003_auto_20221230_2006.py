# Generated by Django 2.2.12 on 2022-12-30 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authtest', '0002_subject_delete_card_delete_folder1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
