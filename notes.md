# Resumo de Comandos do UV

## Criar ambiente virtual

- `curl -LsSf https://astral.sh/uv/install.sh | sh` - Install UV

- `uv init`: Inicializa um novo projeto gerenciado pelo uv, criando o ambiente virtual e arquivos de configuração (como `pyproject.toml`).
- `uv venv`: Cria um novo ambiente virtual python isolado no diretório atual (geralmente em `.venv`).

- `source .venv/bin/activate` ativar a venv

- `$ uv pip install -r requirements.txt` - Install Python dependencies 

## Instalação dos requirements

- `uv add django`: Adiciona o pacote Django como dependência do projeto e o instala no ambiente virtual automaticamente.
- `uv list` / `uv pip list`: Lista todos os pacotes e dependências instaladas no ambiente atual.

## Criação do Requirements

- `uv pip freeze > requirements.txt`: Cria o arquivo com todas as dependências necessárias ao projeto agora

## Execução do projeto

- `uv run django-admin startproject <nome> .`: Executa o utilitário do Django para criar a estrutura inicial do projeto no diretório atual. O "." é para não criar uma outra pasta config dentro da pasta config

- `uv run python manage.py startapp <nome>`: Cria a estrutura de um novo aplicativo dentro do projeto Django.

- `uv run python manage.py makemigrations`: Gera os arquivos de migração baseados nas alterações feitas nos modelos do projeto.

- `uv run python manage.py migrate`: Aplica as migrações geradas no banco de dados.

- `uv run python manage.py createsuperuser`: Inicia o prompt para criação de um usuário administrador para acessar o painel administrativo (Admin) do Django.

- `uv run python manage.py runserver`: Inicia o servidor de desenvolvimento local do Django para rodar o projeto.

## Comandos Django - Aula 1 (Framework-aula-1.pdf)

- `uv run python -m django --version`: Verifica se o Django está instalado e exibe a versão atual.

- `uv run python manage.py makemigrations exemplo01`: Gera os arquivos de migração para o app `exemplo01` especificamente, com base nas alterações feitas no seu `models.py`.

- `uv run python manage.py migrate`: Aplica ao banco de dados todas as migrações pendentes do projeto.

- `uv run python manage.py createsuperuser`: Cria interativamente um usuário administrador para acessar o painel Admin do Django.

- `uv run python manage.py runserver`: Inicia o servidor de desenvolvimento local do Django.

## Comandos Django - Aula 2 (Framework-aula-2.pdf)

- `uv add django-tables2`: Instala o pacote `django-tables2`, que permite criar tabelas HTML dinâmicas e paginadas a partir de models ou querysets Django.

- `pip install django-bootstrap-v5`: Instala o pacote de integração do Bootstrap 5 com Django (via tags de template). Observação: este pacote suporta apenas Django até a versão 4.x. Em projetos com Django 5+, use Bootstrap via CDN diretamente nos templates HTML.

## Comandos Django - Aula 3 (Framework-aula-3.pdf)

### Instalação de Dependências

- `uv pip install pandas`: Instala a biblioteca Pandas para manipulação de dados e exportação/importação de CSV.

### Migrações de Banco de Dados

- `uv run python manage.py makemigrations exemplo01`: Gera arquivos de migração para o app `exemplo01` com base nas alterações nos modelos (adicionando `procedimento` e `procedimento_executado`).
- `uv run python manage.py migrate`: Aplica as migrações pendentes ao banco de dados.

### Django ORM - Shell Interativo

- `uv run python manage.py shell`: Abre um shell interativo do Django para executar comandos ORM manualmente.

### Consultas ORM (executadas no shell ou em views)

```python
# Importar modelos
from exemplo01.models import Pessoa, procedimento, procedimento_executado
from django.db.models import Q

# Buscar todos os registros
Pessoa.objects.all()

# Retornar colunas específicas
Pessoa.objects.values('nome', 'email')
Pessoa.objects.values_list('nome', 'email')

# Filtrar registros (equivale ao WHERE)
Pessoa.objects.filter(funcao="Médico")
Pessoa.objects.filter(funcao="Médico", ativo=True)

# Filtro com OR (usando Q)
query = Q( Q(funcao="Médico") | Q(funcao="Professor") )
Pessoa.objects.filter(query)

# Filtro com AND e OR combinados
Pessoa.objects.filter(query, ativo=True)

# EXCLUDE (equivale ao NOT)
Pessoa.objects.filter(nascimento="1980-01-01").exclude(ativo=False)

# ORDER BY
Pessoa.objects.filter(ativo=True).order_by("nome")       # ASC
Pessoa.objects.filter(ativo=True).order_by("-nome")      # DESC

# GET (busca por chave única)
Pessoa.objects.get(nome='Fulano de Tal')

# UPDATE
Pessoa.objects.filter(id=1).update(nome='Novo Nome')
Pessoa.objects.update(ativo=True)

# EXISTS
Pessoa.objects.filter(ativo=True).exists()

# COUNT
Pessoa.objects.filter(ativo=True).count()

# FIRST e LAST
Pessoa.objects.filter(ativo=True).first()
Pessoa.objects.filter(ativo=True).last()

# IN
Pessoa.objects.filter(id__in=[1, 2, 3, 4, 5])

# Comparações
Pessoa.objects.filter(id__gt=5)    # Maior que
Pessoa.objects.filter(id__gte=5)   # Maior ou igual
Pessoa.objects.filter(id__lt=5)    # Menor que
Pessoa.objects.filter(id__lte=5)   # Menor ou igual

# STARTSWITH
Pessoa.objects.filter(nome__startswith='Jo')

# CONTAINS
Pessoa.objects.filter(nome__contains='Jo')

# Consultas entre tabelas (usando ForeignKey)
procedimento_executado.objects.filter(pessoa__ativo=True)
procedimento_executado.objects.filter(pessoa__ativo=True, procedimento__cid=512)

# Ver SQL gerado
reg = procedimento_executado.objects.filter(pessoa__ativo=True, procedimento__cid=512)
print(str(reg.query))

# Acesso aos campos relacionados
reg = procedimento_executado.objects.filter(pessoa__ativo=True, procedimento__cid=512)
print(reg[0].pessoa.celular)
print(reg[0].procedimento.valor)
```

# FIRST e LAST

Pessoa.objects.filter(ativo=True).first()
Pessoa.objects.filter(ativo=True).last()

# IN

Pessoa.objects.filter(id\_\_in=[1, 2, 3, 4, 5])

# Comparadores: GT, GTE, LT, LTE

Pessoa.objects.filter(id**gt=5)
Pessoa.objects.filter(id**lt=5)
Pessoa.objects.filter(id**gte=5)
Pessoa.objects.filter(id**lte=5)

# STARTSWITH e CONTAINS

Pessoa.objects.filter(nome**startswith='Jo')
Pessoa.objects.filter(nome**contains='Jo')

# Consultas entre tabelas (JOIN via ForeignKey)

procedimento_executado.objects.filter(pessoa**ativo=True)
procedimento_executado.objects.filter(pessoa**ativo=True, procedimento\_\_cid=512)

# Verificar SQL gerado pelo Django

reg = procedimento_executado.objects.filter(pessoa\_\_ativo=True)
print(str(reg.query))

````

### Instalação do Pandas
- `uv add pandas`: Instala o Pandas para manipulação e exportação/importação de dados (CSV, Excel, etc.)

### Migrações após adicionar novas tabelas (procedimento, procedimento_executado)
- `uv run python manage.py makemigrations exemplo01`: Gera migrações para as novas tabelas adicionadas em models.py.
- `uv run python manage.py migrate`: Aplica as migrações ao banco de dados.


## Comandos Django - Aula 4 (Framework-aula-4.pdf)

### Novo App exemplo02
- `uv run python manage.py startapp exemplo02`: Cria a estrutura do novo aplicativo exemplo02.

### Models Criados (exemplo02/models.py)
- **Medico**: nome, especialidade, crm, telefone, email
- **Paciente**: nome, data_nascimento, cpf, telefone, email
- **Procedimento**: descricao, codigo, valor
- **Consulta**: paciente, medico, procedimento, data_consulta, Observacao

### Views Criadas (exemplo02/views.py)
- `listamedico`: Lista todos os médicos
- `listaPaciente`: Lista todos os pacientes
- `detalheConsulta`: Detalhes das consultas (usando select_related para JOIN)
- `novaConsulta`: Formulário para criar nova consulta (POST)

### URLs (exemplo02/urls.py)
- `/exemplo02/listamedico/`
- `/exemplo02/listaPaciente/`
- `/exemplo02/detalheConsulta/`
- `/exemplo02/novaConsulta/`

### Consultas Avançadas no Shell
```python
from exemplo02.models import Medico, Paciente, Procedimento, Consulta

# JOIN com select_related (otimiza consultas)
consultas = Consulta.objects.select_related('paciente', 'medico', 'procedimento').all()

# Filtrar por relacionamento
Consulta.objects.filter(medico__especialidade='Cardiologia')

# Agregações
from django.db.models import Count, Sum, Avg
Consulta.objects.filter(medico__nome='Dr. João').count()
Consulta.objects.values('procedimento__descricao').annotate(total=Sum('valor'))
````

### Geração de Migrações para exemplo02

- `uv run python manage.py makemigrations exemplo02`: Gera as migrações para as novas tabelas.
- `uv run python manage.py migrate`: Aplica ao banco.

### Importação e Exportação de Dados (TXT/CSV)

#### Novo Modelo: exame
- Adicionado em `exemplo01/models.py`:
```python
class exame(models.Model):
    valor = models.FloatField(null=True, blank=True, default=None, verbose_name='Valor')
    def __str__(self):
        return str(self.valor)
```

#### Migrações para exame
- `uv run python manage.py makemigrations exemplo01`: Gera migração para o modelo exame.
- `uv run python manage.py migrate`: Aplica a migração.

#### Instalação do Plotly para Gráficos
- `uv pip install plotly`: Instala a biblioteca Plotly para criação de gráficos interativos.

#### Ambiente Virtual (Replicação)

- `python -m pip freeze > requirements.txt`: Gera lista de dependências instaladas (adaptado para UV: `uv pip freeze > requirements.txt`).
- `python -m venv <nome_env>`: Cria novo ambiente virtual (UV: `uv venv`).
- `python -m pip install -r requirements.txt`: Instala dependências no novo ambiente (UV: `uv pip install -r requirements.txt`).
