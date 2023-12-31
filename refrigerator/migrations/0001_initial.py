# Generated by Django 4.0.6 on 2023-07-26 06:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        ('cook', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Refrigerator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('add_date', models.DateField(auto_now_add=True)),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cook.ingredient')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
            options={
                'verbose_name': '냉장고',
                'verbose_name_plural': '냉장고',
                'db_table': 'sumyo_refrigerator',
            },
        ),
    ]
