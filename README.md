
# 🎓 Sistema de Gestão de Clubes e Grupos Acadêmicos (SGA)
## 🌟 Visão Geral do Projeto (README)
Este projeto é uma aplicação web desenvolvida em Django e Python com foco nos princípios de Rapid Application Development (RAD). 
O objetivo é fornecer uma plataforma centralizada e eficiente para a criação, gestão de membros, e acompanhamento de projetos e eventos em Clubes e Grupos de Extensão Acadêmica.


# Funcionalidades Chave (CRUD)

|Módulo          |Funcionalidades                |Permissão|
|----------------|-------------------------------|-----------------------------|
|Autenticação|Login, Registo de Usuários, Logout.            |Público
|Clubes            |Criação, Visualização (Detalhes), Edição, Exclusão.           |Privado (`@login_required`)
|Membros|Adicionar/Remover Membro, Mudança de Cargo (Membro, Gerente).    |`Advisor` (Dono) / `Manager`            |
|Projetos/Eventos|Criação, Visualização de Detalhes, Edição de Status (Projetos).|`Advisor` / `Manager`|
|Interface|Dashboard Personalizado (separa Clubes que Lidera/Participa).|`Advisor` / `Member`|



# 🛠️ Tecnologias Utilizadas
|  Categoria    |  Tecnologia      |   Uso     |
|-------------|------------------|------------------------------|
|Framework    |   Python 3.9+    |Linguagem de Back-end principal.
|Web Framework|   Django 4.x   |Desenvolvimento rápido de aplicações web (MVT/RAD).
|Banco de Dados|   SQLite3 (Desenvolvimento)    |Banco de dados leve, ideal para RAD e prototipagem local.
|Estilização|  HTML5 / CSS3 Puro   |Design Responsivo (Mobile-First) e Estilos Customizados. 

# Modelagem do Projeto
<img width="1812" height="933" alt="SGA modelagem" src="https://github.com/user-attachments/assets/5d7a4285-2333-46a3-a32b-09aa336a6f9c" />



# ⚙️ Guia de Configuração e Instalação
**Siga estes passos para ter o projeto rodando localmente (ambiente de desenvolvimento).**

**1. Clonar o Repositório**
````Bash
# Clone o projeto do GitHub
git clone https://github.com/Clay1442/-Sistema-de-Grupos-Acad-micos-SGA-.git
# Entre na pasta do projeto 
cd [NOME-DO-PROJETO]
````
**2. Configurar o Ambiente Virtual (venv)**
É crucial isolar as dependências do projeto.
````Bash
# Cria o ambiente virtual 
python -m venv venv

# Ativa o ambiente virtual
# Windows:
.\venv\Scripts\activate

# macOS/Linux:
source venv/bin/activate
````

**3. Instalar as Dependências**
Instale todos os pacotes necessários listados no requirements.txt
````Bash
# O arquivo deve conter: Django, Pillow, gunicorn, etc.
pip install -r requirements.txt
````

**4. Configurar e Executar**
Como você usou SQLite, o banco de dados principal já estará no arquivo db.sqlite3 (se você o copiou). Caso contrário, execute os comandos para criar o banco do zero:
````Bash
# 1. Aplicar Migrações (Cria as tabelas no SQLite)
python manage.py migrate

# 2. Criar Conta de Superusuário (Para acessar /admin/ e criar dados de teste)
python manage.py createsuperuser

# 3. Rodar o Servidor de Desenvolvimento
python manage.py runserver
````

