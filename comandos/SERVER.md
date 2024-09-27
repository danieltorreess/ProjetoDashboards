Configuração para deploy

Primeiros passos
Prepare o local_settings.py
Crie o seu servidor Ubuntu 20.04 LTS (onde preferir)~

Comando para gerar SECRET_KEY
python -c "import string as s;from secrets import SystemRandom as SR;print(''.join(SR().choices(s.ascii_letters + s.digits + s.punctuation, k=64)));"

Criando sua chave SSH
ssh-keygen -C 'COMENTÁRIO'

No servidor
ssh usuário@IP_SERVIDOR

Comandos iniciais
sudo apt update -y
sudo apt upgrade -y
sudo apt autoremove -y
sudo apt install build-essential -y

sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install python3.11 python3.11-venv -y

sudo apt install nginx -y
sudo apt install certbot python3-certbot-nginx -y
sudo apt install postgresql postgresql-contrib -y
sudo apt install libpq-dev -y
sudo apt install git -y

Configurando o git
git config --global user.name 'Seu nome'
git config --global user.email 'seu_email@gmail.com'
git config --global init.defaultBranch main

Criando as pastas do projeto e repositório
mkdir ~/dashboardrepo ~/dashboardapp

Configurando os repositórios
cd ~/dashboardrepo
git init --bare
cd ..
cd ~/dashboardapp
git init
git remote add dashboardrepo ~/dashboardrepo
git add .
git commit -m 'Initial'
git push dashboardrepo main -u # erro

No seu computador local
git remote add dashboardrepo cicero@34.132.171.16:~/dashboardrepo
git push dashboardrepo main
$env:GIT_SSH_COMMAND="ssh -i ~/.ssh/danieltorres_rsa" git push dashboardrepo main

No servidor
cd ~/dashboardapp
git pull dashboardrepo main

Configurando o Postgresql
sudo -u postgres psql

postgres=# create role usuario_dashboard with login superuser createdb createrole password 'senha_usuario_dashboard';
CREATE ROLE
postgres=# create database projeto_dashboard with owner usuario_dashboard;
CREATE DATABASE
postgres=# grant all privileges on database projeto_dashboard to usuario_dashboard;
GRANT
postgres=# \q

sudo systemctl restart postgresql

Criando o local_settings.py no servidor
nano ~/dashboardapp/project/local_settings.py

Cole os dados.

Configurando o Django no servidor
cd ~/dashboardapp
python3.11 -m venv venv
. venv/bin/activate
pip install --upgrade pip
pip install django
pip install pillow
pip install gunicorn
pip install psycopg
pip install faker

python manage.py runserver
python manage.py migrate
python manage.py collectstatic
python manage.py createsuperuser

Permitir arquivos maiores no nginx
sudo nano /etc/nginx/nginx.conf

Adicione em http {}:
client_max_body_size 30M;
sudo systemctl restart nginx
