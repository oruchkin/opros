# Generated by Django 2.2.10 on 2021-09-04 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_opros_question_1variant_question_tekst'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question_tekst',
            name='question_answer',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]