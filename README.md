# OC Lettings

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.12 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/Franco-DevPy/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement : `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel : `which python`
- Confirmer que la version de l'interpréteur Python est la version 3.12 ou supérieure : `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel : `which pip`
- Pour désactiver l'environnement : `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install -r requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest --cov=. --cov-fail-under=80`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel : `.\venv\Scripts\Activate.ps1`
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

---

## Déploiement

Le déploiement est effectué automatiquement via GitHub Actions à chaque push sur la branche `master`.

### Pipeline CI/CD

Les étapes sont les suivantes :

1. **Tests & Linting** — flake8 vérifie la conformité PEP8 et pytest exécute les tests avec un minimum de 80% de couverture. Si cette étape échoue, le déploiement est annulé.

2. **Build & Push Docker** — une image Docker est construite et taguée avec le SHA du commit, puis poussée sur Docker Hub :
   - `francodevd/oc-lettings:<sha_du_commit>`
   - `francodevd/oc-lettings:latest`

3. **Déploiement sur Render** — un appel HTTP au Deploy Hook de Render déclenche le téléchargement de la nouvelle image et le redémarrage du service.

### Variables d'environnement requises

Les variables suivantes doivent être configurées dans le dashboard Render :

| Variable | Description |
|---|---|
| `SECRET_KEY` | Clé secrète Django |
| `DEBUG` | `False` en production |
| `ALLOWED_HOSTS` | `.onrender.com` |
| `SENTRY_DSN` | DSN Sentry pour le monitoring des erreurs |

### Secrets GitHub requis

Les secrets suivants doivent être configurés dans Settings > Secrets and variables > Actions :

| Secret | Description |
|---|---|
| `DOCKER_USERNAME` | Nom d'utilisateur Docker Hub |
| `DOCKER_PASSWORD` | Token d'accès Docker Hub |
| `RENDER_DEPLOY_HOOK` | URL du Deploy Hook Render |

### Exécuter l'application avec Docker

Pour récupérer et lancer l'image directement depuis Docker Hub :

```bash
docker pull francodevd/oc-lettings:latest
docker run -p 8000:8000 francodevd/oc-lettings:latest
```

### Liens

- Site en production : https://oc-lettings-latest-nb04.onrender.com
- Documentation : https://python-oc-lettings-ocr.readthedocs.io/
- Pipeline CI/CD : https://github.com/Franco-DevPy/Python-OC-Lettings-FR/actions
