# Generated by Django 2.2 on 2019-07-28 23:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0012_auto_20190701_0000'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='workflow.Organization'),
        ),
    ]
