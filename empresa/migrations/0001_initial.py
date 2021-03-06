# Generated by Django 3.1.1 on 2020-12-11 03:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('razon_social', models.CharField(max_length=255)),
                ('nit', models.IntegerField(unique=True)),
                ('direccion', models.TextField(null=True)),
                ('ciudad', models.TextField(null=True)),
                ('departamento', models.TextField(null=True)),
                ('logo', models.ImageField(upload_to='cars')),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_estado', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.TextField(max_length=50, null=True)),
                ('apellidos', models.TextField(max_length=50, null=True)),
                ('celular', models.IntegerField()),
                ('whatsapp', models.IntegerField(null=True)),
                ('correo', models.CharField(max_length=60)),
                ('direccion', models.CharField(max_length=60)),
                ('ciudad', models.TextField(null=True)),
                ('departamento', models.TextField(null=True)),
            ],
            options={
                'verbose_name': 'Persona',
                'verbose_name_plural': 'Personas',
            },
        ),
        migrations.CreateModel(
            name='TipoServicio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Planilla',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.IntegerField(unique=True)),
                ('tipo_servicio', models.TextField(null=True)),
                ('total_envios', models.IntegerField(null=True)),
                ('fecha_estado', models.DateField(max_length=255, null=True)),
                ('fecha_ingreso', models.DateField(max_length=255, null=True)),
                ('empresa_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='empresa_repair', to='empresa.empresa')),
                ('estado_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='estado_repair', to='empresa.estado')),
                ('persona_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='persona_repair', to='empresa.persona')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='usuario_repair', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('celular', models.CharField(max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Historial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField()),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='historiales', to='empresa.persona')),
            ],
            options={
                'verbose_name': 'Historial',
                'verbose_name_plural': 'Historiales',
            },
        ),
        migrations.CreateModel(
            name='Guia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField(unique=True)),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='guias', to='empresa.persona')),
            ],
            options={
                'verbose_name': 'Guia',
                'verbose_name_plural': 'Guias',
            },
        ),
        migrations.CreateModel(
            name='Evidencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('imagen', models.ImageField(upload_to='cars')),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='evidencias', to='empresa.persona')),
            ],
            options={
                'verbose_name': 'Evidencia',
                'verbose_name_plural': 'Evidencias',
            },
        ),
    ]
