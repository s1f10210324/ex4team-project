# Generated by Django 4.1.4 on 2022-12-30 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authtest', '0003_auto_20221230_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
