# Projet-GoldenLine-DataPro

## DEPLOIEMENT
Il est d’abord nécessaire de déployer la base de données MySQL. Pour ce faire, un fichier nommé **db.sql** permettant la construction de celle-ci est fourni dans le dossier **database**.

Une fois la base de données déployée, il faut éditer le fichier nommé **conf.ini** et fournir les informations nécessaires à la connexion à la base de données.
Des valeurs d’exemple sont fournies par défaut.

Il faut ensuite installer les dépendances de l’application via la commande suivante :<br>
```pip install -r requirements.txt```

Finalement, il suffit d’exécuter le fichier nommé **app.py** afin de démarrer l’application, via la commande suivante :<br>
```python app.py```

## UTILISATION
L’application est accessible par navigateur web, via l’adresse de votre hébergeur.
Par défaut, en local, l’adresse est : http://localhost:5000
J'ai hébergé mon application sur pythonanywhere.com à l'adresse suivante : https://thomas0130.pythonanywhere.com/
