# Generated by Django 4.1.7 on 2023-03-16 10:51

from django.db import migrations, models
import froala_editor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_testimonial_alter_career_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='productdetail',
            name='align_image',
            field=models.CharField(choices=[('LEFT', 'LEFT'), ('RIGHT', 'RIGHT')], default='LEFT', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='servicedetail',
            name='align_image',
            field=models.CharField(choices=[('LEFT', 'LEFT'), ('RIGHT', 'RIGHT')], default='LEFT', max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='productdetail',
            name='description',
            field=froala_editor.fields.FroalaField(),
        ),
        migrations.AlterField(
            model_name='servicedetail',
            name='description',
            field=froala_editor.fields.FroalaField(),
        ),
    ]