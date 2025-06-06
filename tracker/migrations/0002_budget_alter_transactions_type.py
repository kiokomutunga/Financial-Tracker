# Generated by Django 5.1.2 on 2025-06-05 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category', models.CharField(choices=[('Food', 'Food'), ('Transport', 'Transport'), ('Housing', 'Housing'), ('Entertainment', 'Entertainment'), ('Other', 'Other')], max_length=100)),
                ('amount', models.FloatField()),
                ('month', models.DateTimeField()),
                ('year', models.DateTimeField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.AlterField(
            model_name='transactions',
            name='Type',
            field=models.CharField(choices=[('expenses', 'Expenses'), ('income', 'Income')], max_length=100),
        ),
    ]
