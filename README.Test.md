# Tests pour PipouBlog

Ce document explique comment nous avons implémenté les tests pour le projet PipouBlog, comment les exécuter localement et comment fonctionne l'intégration continue (CI) pour les tests.

## 🗂️ Architecture des tests

### Framework de test

Nous utilisons le framework de test intégré de Django, qui est basé sur `unittest` de Python. Cette approche a été choisie pour sa simplicité et sa compatibilité directe avec Django, sans besoin de dépendances supplémentaires complexes.

### Structure des tests

- Les tests sont organisés dans les fichiers `tests.py` de chaque application Django
- Actuellement, nous avons des tests basiques pour vérifier le bon fonctionnement des vues principales

### Configuration spéciale pour les tests

Pour faciliter l'exécution des tests sans dépendre d'une base de données PostgreSQL, nous avons créé un fichier de configuration spécifique pour les tests :

- `pipou_blog/pipou_blog/test_settings.py` : Ce fichier contient une configuration Django complète qui :
  - Utilise SQLite en mémoire au lieu de PostgreSQL
  - Désactive les migrations pour accélérer les tests
  - Conserve toutes les autres configurations nécessaires (authentification personnalisée, etc.)

## 🚀 Exécution des tests localement

### Exécuter les tests de base

Pour lancer les tests localement, exécutez la commande suivante depuis le répertoire principal du projet :

```bash
cd pipou_blog
python manage.py test blog --settings=pipou_blog.test_settings
```

Cette commande :
- Crée une base de données SQLite en mémoire temporaire
- Exécute tous les tests trouvés dans l'application `blog`
- Utilise les paramètres de test spécifiques qui évitent les problèmes de connexion PostgreSQL

### Mesurer la couverture de code

Pour mesurer la couverture de code, nous utilisons l'outil `coverage` :

1. Exécuter les tests avec mesure de couverture :
```bash
cd pipou_blog
coverage run manage.py test blog --settings=pipou_blog.test_settings
```

2. Afficher le rapport de couverture en console :
```bash
coverage report
```

3. Générer un rapport HTML interactif (plus détaillé) :
```bash
coverage html
```
Puis ouvrez le fichier `htmlcov/index.html` dans votre navigateur.

## 🔄 Intégration Continue (CI)

### Configuration GitHub Actions

Nous avons configuré GitHub Actions pour exécuter automatiquement les tests à chaque push sur les branches `main` et `dev`. Le workflow est défini dans le fichier `.github/workflows/tests.yml` et il :

1. Configure l'environnement Python
2. Installe les dépendances du projet
3. Exécute les tests avec mesure de couverture
4. Génère un rapport de couverture
5. Publie le rapport comme un artefact de build

### Consulter les résultats des tests CI

Après chaque exécution du workflow GitHub Actions :
1. Allez dans l'onglet "Actions" du dépôt GitHub
2. Sélectionnez l'exécution de workflow que vous souhaitez consulter
3. Dans la section "Artifacts", vous pouvez télécharger le rapport de couverture XML

## 📝 Écrire de nouveaux tests

### Créer un test simple

Pour ajouter un nouveau test, modifiez ou créez un fichier `tests.py` dans votre application Django :

```python
from django.test import TestCase
from django.urls import reverse

class VotreTestCase(TestCase):
    def setUp(self):
        # Code exécuté avant chaque test
        pass
        
    def test_exemple(self):
        # Votre test ici
        response = self.client.get(reverse('nom-de-la-vue'))
        self.assertEqual(response.status_code, 200)
```

### Bonnes pratiques pour les tests

1. **Isolation** : Chaque test doit être indépendant des autres
2. **Nommage clair** : Nommez vos tests de façon descriptive (`test_user_can_login` plutôt que `test1`)
3. **Tests atomiques** : Chaque test ne doit vérifier qu'un seul comportement
4. **Fixtures** : Utilisez `setUp()` pour préparer les données de test
5. **Couverture complète** : Testez les cas de succès ET d'erreur

## 🔍 Dépannage

### Problèmes courants

- **ImportError** : Vérifiez que les imports correspondent à la structure du projet
- **Erreurs de base de données** : Assurez-vous d'utiliser `--settings=pipou_blog.test_settings`
- **Échecs de test** : Vérifiez les messages d'erreur et assurez-vous que les conditions testées sont correctes

## 📈 Évolution future des tests

À mesure que le projet évolue, nous prévoyons d'ajouter :

1. **Tests unitaires** pour tous les modèles et fonctions
2. **Tests d'intégration** pour vérifier les interactions entre composants
3. **Tests fonctionnels** pour simuler des scénarios utilisateur complets
4. **Tests de performance** pour vérifier la rapidité de l'application sous charge

---

N'hésitez pas à enrichir cette documentation au fur et à mesure que vous ajoutez de nouveaux tests ou que vous améliorez la configuration de test.
