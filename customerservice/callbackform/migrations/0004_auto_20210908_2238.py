# Generated by Django 3.2.7 on 2021-09-08 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('callbackform', '0003_auto_20210908_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supportrequest',
            name='company_name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='supportrequest',
            name='email',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='supportrequest',
            name='phone_number',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='supportrequest',
            name='sender_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='supportrequest',
            name='subject',
            field=models.CharField(max_length=50),
        ),
    ]
