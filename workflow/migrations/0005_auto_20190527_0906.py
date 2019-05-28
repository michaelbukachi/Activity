# Generated by Django 2.2.1 on 2019-05-27 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0004_auto_20190525_0205'),
    ]

    operations = [
        migrations.AddField(
            model_name='activityuser',
            name='organizations',
            field=models.ManyToManyField(blank=True, null=True, related_name='organization', to='workflow.Organization', verbose_name='Accessible Organizations'),
        ),
        migrations.AlterField(
            model_name='activityuser',
            name='organization',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='workflow.Organization'),
        ),
    ]