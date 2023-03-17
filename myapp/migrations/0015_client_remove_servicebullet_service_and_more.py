# Generated by Django 4.1.7 on 2023-03-17 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_information_experience'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('logo', models.ImageField(upload_to='testimonial')),
            ],
        ),
        migrations.RemoveField(
            model_name='servicebullet',
            name='service',
        ),
        migrations.DeleteModel(
            name='ProductBullet',
        ),
        migrations.DeleteModel(
            name='ServiceBullet',
        ),
    ]
