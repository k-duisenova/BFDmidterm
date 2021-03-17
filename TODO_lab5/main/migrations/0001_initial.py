# Generated by Django 3.1.7 on 2021-03-17 05:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('due_on_date', models.DateTimeField()),
                ('owner', models.CharField(max_length=100)),
                ('category', models.CharField(default='Incomplete', max_length=40)),
                ('list_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='todos', to='main.todolist')),
            ],
        ),
    ]
