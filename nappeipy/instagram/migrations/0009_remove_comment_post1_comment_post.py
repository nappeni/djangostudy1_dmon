# Generated by Django 4.1.7 on 2023-04-02 05:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0008_rename_post_comment_post1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='post1',
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='instagram.post'),
            preserve_default=False,
        ),
    ]
