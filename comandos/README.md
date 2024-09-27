# Estrutura do meu projeto
ProjetoDashboards/
    comandos/
        gitbash.txt
        README.md
    dashboard/
        migrations/
            __init__.py
        static/
            css/
                powerbi.css
                profile.css
                usuario.css
                header.css
            img/
                AraFariaLima.png
                Dashboard.png
                DP.png
                Financeiro.png
                Gerenciamento.png
                Indicadores.png
                Indices.png
                Logout.png
                MV.png
                Processos.png
                SubMenu.png
                Suprimentos.png
                TI.png
                Usuario.png
                Visna.png
        templates/
            base.html
            powerbi.html
            profile.html
            usuario.html
            header.html
        __init__.py
        admin.py
        apps.py
        models.py
        tests.py
        urls.py
        views.py
    project/
        __init__.py
        asgi.py
        settings.py
        urls.py
        wsgi.py
    venv/
    .gitignore
    db.sqlite3
    manage.py


    staticfiles/
        admin/
        css/
            powerbi.css
            profile.css
            usuario.css
        img/
            AraFariaLima.png
            Dashboard.png
            DP.png
            Financeiro.png
            Gerenciamento.png
            Indicadores.png
            Indices.png
            Logout.png
            MV.png
            Processos.png
            SubMenu.png
            Suprimentos.png
            TI.png
            Usuario.png
            Visna.png


# Criação do projeto
python -m venv venv 
.\venv\Scripts\activate
pip install django
python.exe -m pip install --upgrade pip
django-admin startproject dashboard
cd projetodashboard
django-admin startapp dashboard
python manage.py collectstatic
python manage.py runserver
python manage.py migrate
python manage.py showmigrations

# Criação do superuser no Admin do Django
python manage.py createsuperuser

cicero.torres@mvconstrucoes.com.br - @Mva2022
marcelo@mvconstrucoes.com.br - @Mva2024
beretta@mvconstrucoes.com.br - @Mva2024

# Deploy
cd ~/.ssh
ls
PS C:\Users\Cicero> cd ~/.ssh
PS C:\Users\Cicero\.ssh> ls


    Diretório: C:\Users\Cicero\.ssh


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----        30/07/2024     10:42           3381 danieltorres_rsa
-a----        30/07/2024     10:42            739 danieltorres_rsa.pub
-a----        30/07/2024     09:58            828 known_hosts
-a----        30/07/2024     09:58             92 known_hosts.old
cat ~/.ssh/danieltorres_rsa.pub
ssh -i ~/.ssh/danieltorres_rsa cicero@34.132.171.16
* exit *


