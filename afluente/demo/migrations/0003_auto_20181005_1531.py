# Generated by Django 2.0.8 on 2018-10-05 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0002_cliente_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='servico',
            field=models.CharField(choices=[('HOSP', 'Hospedagem'), ('MAIL', 'E-mail'), ('HOSPMAIL', 'Hospedagem e E-mail')], max_length=1),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='status',
            field=models.CharField(choices=[('AT', 'Ativo'), ('INAT', 'Inativo')], max_length=1),
        ),
    ]