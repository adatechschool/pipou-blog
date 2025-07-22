"""
Configuration spécifique pour les tests Django.
Ce fichier étend la configuration principale mais utilise SQLite pour les tests.
"""

from .settings import *

# Configuration de la base de données pour les tests
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

# Désactiver la migration pour les tests pour améliorer la performance
# et éviter les problèmes avec les bases de données externes
class DisableMigrations:
    def __contains__(self, item):
        return True

    def __getitem__(self, item):
        return None

MIGRATION_MODULES = DisableMigrations()
