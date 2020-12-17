# Generated by Django 3.1.4 on 2020-12-17 01:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mystore', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100)),
                ('price', models.IntegerField(default=0)),
                ('description', models.TextField(blank=True, max_length=200, null=True)),
                ('image', models.ImageField(upload_to='uploads/products/')),
                ('cate_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categoryid', to='mystore.category')),
            ],
        ),
    ]