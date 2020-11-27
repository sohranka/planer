# Generated by Django 3.1.3 on 2020-11-26 14:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dailyplan', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DaysTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='MyDay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_date', models.DateField(unique=True)),
                ('owner', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('status', models.BooleanField(default=False)),
                ('days', models.ManyToManyField(blank=True, null=True, through='dailyplan.DaysTask', to='dailyplan.MyDay')),
                ('owner', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Schedule',
        ),
        migrations.AddField(
            model_name='myday',
            name='tasks',
            field=models.ManyToManyField(blank=True, null=True, through='dailyplan.DaysTask', to='dailyplan.Task'),
        ),
        migrations.AddField(
            model_name='daystask',
            name='day',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dailyplan.myday'),
        ),
        migrations.AddField(
            model_name='daystask',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dailyplan.task'),
        ),
    ]