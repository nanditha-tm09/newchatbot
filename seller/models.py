from django.db import migrations, models

# Create your models here.


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=20)),
                ('pic', models.ImageField(upload_to='seller/')),
                ('login_id', models.IntegerField()),
                ('password', models.CharField(max_length=20)),
                ('status', models.CharField(default='pending', max_length=20)),
            ],
            options={
                'db_table': 'seller_tb',
            },
        ),
]