# Generated by Django 3.0 on 2019-12-13 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=100)),
                ('time', models.FloatField()),
            ],
        ),
        migrations.AddIndex(
            model_name='exam',
            index=models.Index(fields=['id'], name='exam_exam_id_5eaed9_idx'),
        ),
    ]