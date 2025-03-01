# Generated by Django 3.2.5 on 2021-10-17 19:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('topicblog', '0013_alter_topicblogitem_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='TopicBlogContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_type', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='topicblogitem',
            name='item_type',
        ),
        migrations.AlterField(
            model_name='topicblogtemplate',
            name='template_name',
            field=models.CharField(max_length=80, unique=True),
        ),
        migrations.AddField(
            model_name='topicblogitem',
            name='content_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='topicblog.topicblogcontenttype'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='topicblogtemplate',
            name='content_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='topicblog.topicblogcontenttype'),
        ),
    ]
