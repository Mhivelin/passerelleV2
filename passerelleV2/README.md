# Passerelle DELTIC

## Description
Le but de ce projet est de créer une plateforme de gestion passerelle pour les données des clients de deltic.

## Installation
Pour installer le projet, il suffit de cloner le docker et de lancer la commande `docker-compose up` pour lancer le projet.

## Utilisation
Pour utiliser le projet, il suffit de se rendre sur l'adresse `http://XXXXXXXXX:5000` pour accéder à l'interface web.

## presentation de la plateforme
La plateforme est composée de 3 parties sous la forme MVC (Model View Controller) :

### Model
Le model est la partie qui gère les données. Il est composé de 2 parties :
- La base de données : C'est la partie qui stocke les données des clients.
- les classes : C'est la partie qui gère les données 

### View
La vue est la partie qui gère l'interface utilisateur. Elle est composée de 2 parties :
- Les templates : Ce sont les éléments qui sont communs à toutes les pages web.
- Les fichiers statiques : Ce sont les fichiers qui sont utilisés pour la mise en forme des pages web.

### Controller
Le controller est la partie qui gère les requêtes de l'utilisateur, ce sont les routes qui permettent de rediriger l'utilisateur vers la bonne page.

## Auteurs
- [Marius Hivelin]()