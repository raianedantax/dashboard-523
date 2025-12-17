Projeto Base - Dashboard Acadêmico

Este é o projeto-base para a disciplina de Engenharia de Software, utilizando Django para consumir e analisar um banco de dados acadêmico legado.

Como Configurar o Projeto (Guia do Aluno)

Siga estes passos para executar o projeto na sua máquina local.

1. Pré-requisitos

Python 3.10+

Git

Um servidor MySQL (como XAMPP, MAMP ou MySQL Community Server)

2. Clonar o Repositório

Após usar este template para criar o seu próprio repositório, clone-o para a sua máquina:

git clone [URL_DO_SEU_REPOSITORIO_NO_GITHUB]
cd [nome-do-repositorio]


3. Criar o Ambiente Virtual

É uma boa prática isolar as dependências do projeto.

# Criar o ambiente
python3 -m venv venv

# Ativar o ambiente (macOS/Linux)
source venv/bin/activate

# Ativar o ambiente (Windows)
.\venv\Scripts\activate


4. Instalar as Dependências

As bibliotecas necessárias estão listadas no ficheiro requirements.txt.

pip install -r requirements.txt


5. Configurar o Banco de Dados

Certifique-se de que o seu servidor MySQL está a funcionar.

Crie um novo banco de dados (ex: dashboard_aluno).

Importante: Execute o script SQL (.sql) fornecido pelo professor para criar a estrutura de tabelas legada.

Renomeie o ficheiro env.example (se fornecido) para .env ou edite diretamente o settings.py.

Abra dashboard/settings.py e atualize a secção DATABASES com as suas credenciais:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dashboard_aluno',  # O nome do banco que você criou
        'USER': 'root',             # O seu utilizador do MySQL
        'PASSWORD': 'sua_senha',    # A sua senha do MySQL
        'HOST': 'localhost',
        'PORT': '3306',
    }
}


6. Executar o Projeto

Execute as Migrações do Django: (Isto não irá tocar nas tabelas do banco legado, mas criará as tabelas do Django para utilizadores e sessões).

python manage.py migrate


Crie um Super-Utilizador: (Necessário para aceder ao /admin e ao /dashboard)

python manage.py createsuperuser


Execute o Servidor:

python manage.py runserver


O seu site estará disponível em http://127.0.0.1:8000/dashboard/.# dashboard-523
