# Utiliser une image de base officielle avec Python 3.9
FROM python:3.9-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier le fichier requirements.txt dans le répertoire de travail
COPY requirements.txt /app/

# Installer les dépendances spécifiées dans requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste de l'application dans le répertoire de travail
COPY . .

# Définir les variables d'environnement
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=oc_lettings_site.settings

# Exposer le port 8000
EXPOSE 8000

# Collecter les fichiers statiques
RUN python manage.py collectstatic --noinput

# Lancer le serveur Django
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "oc_lettings_site.wsgi:application"]
