# Generated by Django 5.1.1 on 2024-10-19 18:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="emprestimo",
            name="condicoesEPI",
            field=models.TextField(
                choices=[("Novo", "Novo"), ("Usado", "Usado"), ("Ruim", "Ruim")]
            ),
        ),
        migrations.AlterField(
            model_name="emprestimo",
            name="status",
            field=models.TextField(
                choices=[
                    ("Emprestado", "Emprestado"),
                    ("Em uso", "Em uso"),
                    ("Forneceido", "Fornecido"),
                    ("Devolvido", "Devolvido"),
                    ("Danificado", "Danificado"),
                    ("Perdido", "Perdido"),
                ]
            ),
        ),
    ]
