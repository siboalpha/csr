# Generated by Django 4.1.3 on 2022-12-03 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_alter_blog_blog_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='blog_summary',
            field=models.TextField(default='Lorem ipsum dolor sit amet consectetur adipiscing elit Ut et massa mi. Aliquam in hendrerit urna', max_length=255),
        ),
    ]