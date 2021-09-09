# Generated by Django 3.2.7 on 2021-09-08 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('callbackform', '0002_auto_20210908_2213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supportrequest',
            name='comment',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='supportrequest',
            name='company_name',
            field=models.TextField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='supportrequest',
            name='email',
            field=models.TextField(max_length=50),
        ),
        migrations.AlterField(
            model_name='supportrequest',
            name='phone_number',
            field=models.TextField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='supportrequest',
            name='problem_description',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='supportrequest',
            name='sender_name',
            field=models.TextField(max_length=50),
        ),
        migrations.AlterField(
            model_name='supportrequest',
            name='subject',
            field=models.TextField(max_length=50),
        ),
    ]