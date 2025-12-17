import random
from decimal import Decimal
from django.core.management.base import BaseCommand
from django.db import transaction, connection
from faker import Faker

from dashboard_app.models import (
    AreaDoConhecimento, Curso, Serie, Turno, Disciplina,
    Turma, Aluno, AlunoTurma, Boletim, DisciplinaCursoSerie
)

class Command(BaseCommand):
    help = 'Popula o banco de dados com uma base curricular comum e disciplinas técnicas anuais.'

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Iniciando o povoamento com currículo (Base + Técnica)...'))
        
        fake = Faker('pt_BR')

        with connection.cursor() as cursor:
            self.stdout.write('Desativando a checagem de chaves estrangeiras...')
            cursor.execute("SET FOREIGN_KEY_CHECKS=0;")

        self.stdout.write('Limpando dados antigos...')
        Boletim.objects.all().delete()
        AlunoTurma.objects.all().delete()
        Aluno.objects.all().delete()
        DisciplinaCursoSerie.objects.all().delete()
        Turma.objects.all().delete()
        Disciplina.objects.all().delete()
        AreaDoConhecimento.objects.all().delete()
        Curso.objects.all().delete()
        Serie.objects.all().delete()
        Turno.objects.all().delete()

        self.stdout.write('Criando dados básicos (Cursos, Séries, etc)...')
        areas = {desc: AreaDoConhecimento.objects.create(id=i+1, descricao=desc) for i, desc in enumerate(['Técnica', 'Humanas', 'Matemática', 'Linguagem', 'Natureza'])}
        cursos = {desc: Curso.objects.create(id=i+1, descricao=desc) for i, desc in enumerate(['Técnico em Informática', 'Técnico em Eletrotécnica', 'Técnico em Segurança do Trabalho', 'Técnico em Edificações', 'Ensino Médio'])}
        series = {f'{i}º Ano': Serie.objects.create(id=i, descricao=f'{i}º Ano') for i in range(1, 4)}
        turnos = {desc: Turno.objects.create(id=i+1, descricao=desc) for i, desc in enumerate(['Matutino', 'Vespertino'])}

        # =====================================================================================
        # SEÇÃO 2: DEFINIÇÃO DO CURRÍCULO E CRIAÇÃO DAS DISCIPLINAS
        # =====================================================================================
        self.stdout.write('Criando disciplinas e o currículo (Base + Técnica)...')
        
        # --- LÓGICA ATUALIZADA ---
        # 1. Definimos todas as disciplinas que existem na escola.
        # 2. Definimos a que curso/série cada uma pertence.

        disciplinas_base_comum = [
            # Disciplinas oferecidas em todos os 3 anos
            {'sigla': 'PORT', 'desc': 'Língua Portuguesa', 'area': areas['Linguagem'], 'series': [series['1º Ano'], series['2º Ano'], series['3º Ano']]},
            {'sigla': 'MAT', 'desc': 'Matemática', 'area': areas['Matemática'], 'series': [series['1º Ano'], series['2º Ano'], series['3º Ano']]},
            # Disciplinas oferecidas apenas em alguns anos
            {'sigla': 'HIST', 'desc': 'História', 'area': areas['Humanas'], 'series': [series['1º Ano'], series['2º Ano']]},
            {'sigla': 'GEO', 'desc': 'Geografia', 'area': areas['Humanas'], 'series': [series['1º Ano'], series['2º Ano']]},
            {'sigla': 'FIS', 'desc': 'Física', 'area': areas['Natureza'], 'series': [series['1º Ano'], series['2º Ano'], series['3º Ano']]},
            {'sigla': 'QUIM', 'desc': 'Química', 'area': areas['Natureza'], 'series': [series['1º Ano'], series['2º Ano']]},
            {'sigla': 'FILO', 'desc': 'Filosofia', 'area': areas['Humanas'], 'series': [series['3º Ano']]},
            {'sigla': 'SOCIO', 'desc': 'Sociologia', 'area': areas['Humanas'], 'series': [series['3º Ano']]},
        ]

        disciplinas_tecnicas = [
            # Trilha de Informática
            {'sigla': 'LPOO', 'desc': 'Lógica de Programação', 'area': areas['Técnica'], 'curso': cursos['Técnico em Informática'], 'serie': series['1º Ano']},
            {'sigla': 'BD', 'desc': 'Banco de Dados', 'area': areas['Técnica'], 'curso': cursos['Técnico em Informática'], 'serie': series['2º Ano']},
            {'sigla': 'WEB', 'desc': 'Desenvolvimento Web', 'area': areas['Técnica'], 'curso': cursos['Técnico em Informática'], 'serie': series['3º Ano']},
            # Trilha de Eletrotécnica
            {'sigla': 'CIR1', 'desc': 'Circuitos Elétricos I', 'area': areas['Técnica'], 'curso': cursos['Técnico em Eletrotécnica'], 'serie': series['1º Ano']},
            {'sigla': 'ELEP', 'desc': 'Eletrônica de Potência', 'area': areas['Técnica'], 'curso': cursos['Técnico em Eletrotécnica'], 'serie': series['2º Ano']},
            {'sigla': 'INST', 'desc': 'Instalações Elétricas', 'area': areas['Técnica'], 'curso': cursos['Técnico em Eletrotécnica'], 'serie': series['3º Ano']},
            # Trilha de Segurança do Trabalho
            {'sigla': 'HIG', 'desc': 'Higiene Ocupacional', 'area': areas['Técnica'], 'curso': cursos['Técnico em Segurança do Trabalho'], 'serie': series['1º Ano']},
            {'sigla': 'ERG', 'desc': 'Ergonomia', 'area': areas['Técnica'], 'curso': cursos['Técnico em Segurança do Trabalho'], 'serie': series['2º Ano']},
            {'sigla': 'LEGIS', 'desc': 'Legislação Aplicada', 'area': areas['Técnica'], 'curso': cursos['Técnico em Segurança do Trabalho'], 'serie': series['3º Ano']},
            # Trilha de Edificações
            {'sigla': 'DES', 'desc': 'Desenho Técnico', 'area': areas['Técnica'], 'curso': cursos['Técnico em Edificações'], 'serie': series['1º Ano']},
            {'sigla': 'MATC', 'desc': 'Materiais de Construção', 'area': areas['Técnica'], 'curso': cursos['Técnico em Edificações'], 'serie': series['2º Ano']},
            {'sigla': 'ESTR', 'desc': 'Sistemas Estruturais', 'area': areas['Técnica'], 'curso': cursos['Técnico em Edificações'], 'serie': series['3º Ano']},
        ]

        disciplinas_criadas = {}
        disciplina_id_counter = 1

        # Cria todas as disciplinas
        todas_as_disciplinas_data = disciplinas_base_comum + disciplinas_tecnicas
        for d in todas_as_disciplinas_data:
            if d['sigla'] not in disciplinas_criadas:
                disciplina_obj = Disciplina.objects.create(id=disciplina_id_counter, sigla=d['sigla'], descricao=d['desc'], area_do_conhecimento=d['area'])
                disciplinas_criadas[d['sigla']] = disciplina_obj
                disciplina_id_counter += 1

        # Popula a tabela DisciplinaCursoSerie
        disciplina_curso_serie_a_criar = []
        # 1. Atribui a base comum a TODOS os cursos técnicos
        for curso_tecnico in [c for c in cursos.values() if c.descricao != 'Ensino Médio']:
            for d in disciplinas_base_comum:
                disciplina_obj = disciplinas_criadas[d['sigla']]
                for serie_obj in d['series']:
                    disciplina_curso_serie_a_criar.append(DisciplinaCursoSerie(disciplina=disciplina_obj, curso=curso_tecnico, serie=serie_obj))
        
        # 2. Atribui as disciplinas técnicas específicas
        for d in disciplinas_tecnicas:
            disciplina_obj = disciplinas_criadas[d['sigla']]
            disciplina_curso_serie_a_criar.append(DisciplinaCursoSerie(disciplina=disciplina_obj, curso=d['curso'], serie=d['serie']))

        DisciplinaCursoSerie.objects.bulk_create(disciplina_curso_serie_a_criar)

        # Mapeia disciplinas por grade para fácil acesso
        disciplinas_por_grade = {}
        for dcs in DisciplinaCursoSerie.objects.all().select_related('disciplina', 'curso', 'serie'):
            chave = (dcs.curso_id, dcs.serie_id)
            if chave not in disciplinas_por_grade:
                disciplinas_por_grade[chave] = []
            disciplinas_por_grade[chave].append(dcs.disciplina)

        self.stdout.write('Gerando Turmas, Alunos e Boletins...')
        
        codigos_curso = {curso_obj.id: sigla for curso_obj, sigla in zip(cursos.values(), ['5', '4', 'S', '2', 'M'])}
        aluno_matricula_counter = 2025000001
        
        turmas_a_criar = []
        alunos_a_criar = []
        alunoturma_a_criar = []
        boletins_a_criar = []

        for curso_obj in [c for c in cursos.values() if c.descricao != 'Ensino Médio']:
            for serie_obj in series.values():
                for turno_obj in turnos.values():
                    codigo_turma = f"{codigos_curso[curso_obj.id]}{turno_obj.id}{serie_obj.id}"
                    
                    turma_obj = Turma(
                        id=codigo_turma, ano=2025, descricao=codigo_turma,
                        curso=curso_obj, serie=serie_obj, turno=turno_obj,
                        turma_id=0, turma_ano=0
                    )
                    turmas_a_criar.append(turma_obj)

                    disciplinas_da_turma = disciplinas_por_grade.get((curso_obj.id, serie_obj.id), [])

                    for _ in range(10):
                        aluno_obj = Aluno(
                            matricula=str(aluno_matricula_counter),
                            nome=fake.name()
                        )
                        alunos_a_criar.append(aluno_obj)
                        
                        alunoturma_a_criar.append(AlunoTurma(
                            aluno_matricula=aluno_obj,
                            turma_id=turma_obj.id,
                            turma_ano=turma_obj.ano
                        ))

                        for disciplina_obj in disciplinas_da_turma:
                            boletins_a_criar.append(Boletim(
                                aluno_matricula=aluno_obj,
                                disciplina=disciplina_obj,
                                turma_id=turma_obj.id,
                                turma_ano=turma_obj.ano,
                                bimestre1=Decimal(random.uniform(5.0, 10.0)).quantize(Decimal('0.1')),
                                bimestre2=Decimal(random.uniform(5.0, 10.0)).quantize(Decimal('0.1')),
                                bimestre3=Decimal(random.uniform(5.0, 10.0)).quantize(Decimal('0.1'))
                            ))
                        
                        aluno_matricula_counter += 1

        self.stdout.write('Inserindo dados em massa no banco...')
        Turma.objects.bulk_create(turmas_a_criar)
        Aluno.objects.bulk_create(alunos_a_criar)
        AlunoTurma.objects.bulk_create(alunoturma_a_criar)
        Boletim.objects.bulk_create(boletins_a_criar)

        with connection.cursor() as cursor:
            self.stdout.write('Reativando a checagem de chaves estrangeiras...')
            cursor.execute("SET FOREIGN_KEY_CHECKS=1;")

        self.stdout.write(self.style.SUCCESS('Banco de dados populado com sucesso!'))