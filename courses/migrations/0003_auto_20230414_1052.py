# Generated by Django 3.2.18 on 2023-04-14 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_alter_course_groups'),
    ]

    operations = [
        migrations.RenameField(
            model_name='application',
            old_name='sender',
            new_name='student',
        ),
        migrations.RemoveField(
            model_name='application',
            name='course',
        ),
        migrations.RemoveField(
            model_name='application',
            name='group',
        ),
        migrations.AddField(
            model_name='group',
            name='applications',
            field=models.ManyToManyField(blank=True, related_name='group', to='courses.Application', verbose_name='Заявки'),
        ),
        migrations.AlterField(
            model_name='course',
            name='groups',
            field=models.ManyToManyField(blank=True, related_name='course', to='courses.Group', verbose_name='Группы'),
        ),
    ]
