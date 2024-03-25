# Passerelle DELTIC

## Description
La passerelle DELTIC est un projet qui permettra de faire communiquer plusieurs applications entre elles. Elle est basée sur les différentes API des applications à connecter. ce projet as donc pour but de faciliter la communication ainsi que la mise en place des différentes communications entre les applications.

## Installation
Pour installer la passerelle DELTIC, il suffit de cloner le projet sur votre machine. Ensuite, grace a docker, vous pourrez lancer la passerelle.

## Utilisation
Pour utiliser la passerelle DELTIC, il suffit d'avoir les différentes informations de connexion des applications à connecter. ensuite, il suffit de les renseigner dans le formulaire de configuration de la passerelle. Puis, le l'application se chargera de faire la communication entre les applications en suivant sa routine.

## Les différentes passerelles
### Passerelle 1 : Remontée de paiement (EBP --> Zeendoc)

#### Objectif :
Remonter les paiements effectués dans EBP vers Zeendoc afin de faciliter cette démarche pour les utilisateurs, automatiser le processus et éviter les erreurs de saisie.


#### Paramétrage  :
créer un index de paiement dans Zeendoc

informations requises pour la configuration :
Les informations de connexion à l'API EBP
L'id (EBP Client ID)
Le client secret (EBP Client Secret)
La clé d'abonnement (EBP Subscription Key)ici
Les informations de connexion à l'API Zeendoc
Le login (Zeendoc login)
L'url du client (Zeendoc URL Client)
Le mot de passe (Zeendoc CPassword)

#### Configuration :
Se rendre sur cette page pour ajouter un nouveau client 
Remplir les informations requises 
Valider le formulaire 
Se rendre sur la page de configuration du client
Se connecter à l'API EBP grace au bouton
selectionner les champs requis
EBP_FOLDER_ID : l'identifiant du dossier EBP
ZEENDOC_CLASSEUR : l'identifiant du classeur Zeendoc
Enregistrer les modifications 
Tester la configuration en lançant une routine 

