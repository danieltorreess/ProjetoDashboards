python -m venv venv 
.\venv\Scripts\activate
pip install django
python.exe -m pip install --upgrade pip
django-admin startproject projetodashboard
cd projetodashboard
django-admin startapp dashboard
python manage.py collectstatic
python manage.py runserver
python manage.py migrate
python manage.py showmigrations

python manage.py createsuperuser

cicero.torres@mvconstrucoes.com.br - @Mva2022
marcelo@mvconstrucoes.com.br - @Mva2024
beretta@mvconstrucoes.com.br - @Mva2024




