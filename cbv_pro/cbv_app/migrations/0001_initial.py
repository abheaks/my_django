# Generated by Django 3.0.3 on 2020-03-15 02:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('principal', models.CharField(max_length=256)),
                ('location', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('age', models.PositiveIntegerField()),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='Students', to='cbv_app.School')),
            ],
        ),
    ]
