# Generated by Django 4.2 on 2023-04-27 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_book_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='tags',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='file',
            field=models.FileField(null=True, upload_to='books'),
        ),
        migrations.AlterField(
            model_name='book',
            name='picture',
            field=models.ImageField(null=True, upload_to='books'),
        ),
    ]