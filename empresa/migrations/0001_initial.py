# Generated by Django 4.0.3 on 2022-03-21 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeEmpresa', models.CharField(max_length=96)),
                ('nomeAmigavel', models.CharField(max_length=96)),
                ('cnpj', models.CharField(max_length=24)),
                ('endereco', models.CharField(max_length=96)),
                ('numeroEmpresa', models.CharField(max_length=24)),
                ('cidade', models.CharField(max_length=96)),
                ('estado', models.CharField(max_length=96)),
                ('telefone', models.CharField(blank=True, max_length=24, null=True)),
                ('whatsapp', models.CharField(max_length=24)),
                ('email', models.EmailField(max_length=254)),
                ('facebook', models.CharField(blank=True, max_length=96, null=True)),
                ('instagram', models.CharField(blank=True, max_length=96, null=True)),
                ('canalYoutube', models.CharField(blank=True, max_length=96, null=True)),
                ('analytics', models.CharField(blank=True, max_length=96, null=True)),
                ('ramoAtividade', models.TextField()),
                ('tituloPagina', models.CharField(max_length=96)),
                ('descricaoPagina', models.CharField(max_length=96)),
                ('logotipo', models.TextField()),
                ('scriptHeader', models.TextField()),
                ('scriptBody', models.TextField()),
                ('scriptFooter', models.TextField()),
                ('status', models.CharField(choices=[('on', 'Ativa'), ('off', 'Inativa')], max_length=7)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
