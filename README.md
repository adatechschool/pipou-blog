                                  -*   PipouBlog  *-

-- Description --

PipouBlog est une application web développée avec Django, conçue pour créer, éditer et gérer des posts de blog. Elle offre des fonctionnalités d'authentification (inscription, connexion, déconnexion), de gestion de profils utilisateur avec photos, une interface responsive compatible mobile et desktop, et un bouton flottant pour créer rapidement des posts. Le projet utilise une base de données PostgreSQL et inclut une suite de tests automatisés (96% de couverture) ainsi qu'une configuration CI/CD via GitHub Actions.

Pour des informations détaillées, consultez les notices suivantes :

- NOTICE.docker.md : Instructions pour construire, exécuter et déployer avec Docker.
- NOTICE.Init.md : Guide pour l'initialisation et la configuration du projet.
- NOTICE.test.md : Instructions pour exécuter les tests.



-- Prérequis --

- Git
- Docker
- Docker Compose



-- Cloner le projet --

Clonez le dépôt et accédez au répertoire du projet :

-*  git clone git@github.com:adatechschool/pipou-blog.git  *-
** cd PipouBlog/pipou-blog



-- Construire et exécuter avec Docker --

1 - Assurez-vous que Docker et Docker Compose sont installés et en cours d'exécution.


2 - Construisez et lancez les services (incluant la base de données PostgreSQL) :

** docker-compose up --build


3 - Appliquez les migrations pour configurer la base de données :

** docker-compose exec server python manage.py migrate


4 - (Optionnel) Créez un superutilisateur pour accéder à l'interface d'administration :

** docker-compose exec server python manage.py createsuperuser


5 - (Optionnel) Chargez les données de démonstration :

** docker-compose exec server python manage.py loaddata fixtures/all_data.json


6 - L'application est accessible à : http://localhost:8000.


7 - L'interface d'administration est disponible à : http://localhost:8000/admin.

Pour des instructions détaillées sur la configuration Docker, consultez NOTICE.docker.md et NOTICE.Init.md.



-- Déploiement sur le cloud --


1 - Construisez l'image Docker :

** docker build -t pipoublog .

Si votre cloud utilise une architecture différente (par exemple, amd64 pour un Mac M1) :

** docker build --platform=linux/amd64 -t pipoublog .


2 - Poussez l'image vers votre registre :

** docker push myregistry.com/pipoublog

Pour plus de détails, consultez NOTICE.docker.md ou la documentation officielle de Docker.



-- Tests --

Le projet inclut une suite de tests automatisés avec une couverture de 96%. Pour exécuter les tests localement ou configurer l'intégration continue avec GitHub Actions, consultez NOTICE.test.md.

-- Structure du projet

pipou-blog/
├── pipou_blog/           # Configuration Django
├── blog/                 # Application blog
├── authentication/       # Application authentification
├── user_profile/        # Application profils utilisateur
├── static/              # Fichiers statiques (CSS, JS, images)
├── templates/           # Templates HTML
├── fixtures/            # Données de démonstration
├── requirements.txt     # Dépendances Python
├── compose.yaml         # Configuration Docker
└── manage.py            # Script de gestion Django

-- Fonctionnalités principales --

- Authentification : Inscription, connexion, déconnexion.
- Blog : Création, édition, suppression de posts.
- Profils utilisateur : Gestion des profils avec photos.
- Interface responsive : Compatible mobile et desktop.
- Bouton flottant : Création rapide de posts.
- Tests automatisés : Couverture de 96%.
- CI/CD : Configuré avec GitHub Actions.


-- Contribution --

1 - Forkez le projet.
2 - Créez une branche pour votre fonctionnalité.
3 - Committez vos changements.
4 - Poussez vers la branche.
5 - Ouvrez une Pull Request.

Pour plus de détails, consultez NOTICE.Init.md.




