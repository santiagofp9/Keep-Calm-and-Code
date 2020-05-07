# Generated by Django 2.2.12 on 2020-05-07 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tomillo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='prensa',
            options={'ordering': ['-fecha'], 'verbose_name': 'Prensa', 'verbose_name_plural': 'Prensa links'},
        ),
        migrations.AddField(
            model_name='prensa',
            name='body',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='prensa',
            name='order',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='prensa',
            name='slug',
            field=models.SlugField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='prensa',
            name='descripcion',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='prensa',
            name='fecha',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='prensa',
            name='imagen',
            field=models.ImageField(default='pic_folder/None/partner-3.png', upload_to='prensa/'),
        ),
        migrations.AlterField(
            model_name='prensa',
            name='titulo',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
