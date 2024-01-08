# stage DELTIC

## Présentation de l'entreprise

|             |                                                                                |
| ----------- | ------------------------------------------------------------------------------ |
| Nom         | DELTIC                                                                         |
| Description | DELTIC est une entreprise spécialisée dans la dématérialisation des documents. |
| utilisateur | Plus de 165 entreprises utilisent les services de DELTIC.                      |
| Pôles       | CLIENT (4 personnes)                                                           |
|             | SALES (4 personnes)                                                            |
|             | MARKET (6 personnes)                                                           |


## Présentation du projet
Aujourd'hui, tout les documents sont dématérialisés grace a Zeendoc et pour valider les factures (BAP) et donc les envoyers vers des logiciels de comptabilité, les utilisateurs doivent transférer les informations de Zeendoc vers le logiciel de comptabilité (SAGE100 ...) manuellement. Ce projet a pour but de créer une API qui permettra de valider les factures automatiquement.


## journal de bord
### Semaine 1 (22/05 au 26/05):
J'ai commencé mon stage chez DELTIC et j'ai été introduit à l'équipe et aux locaux de l'entreprise. J'ai également été présenté au logiciel Zeendoc, qui est au centre du projet sur lequel je vais travailler. J'ai utilisé cette semaine pour me familiariser avec la documentation développeur de Zeendoc afin de comprendre son fonctionnement.

Un compte sur le site de Zeendoc m'a été créé pour que je puisse accéder à l'interface de gestion des documents. J'ai pu explorer les différentes fonctionnalités de Zeendoc et j'ai commencé à comprendre comment le logiciel fonctionne.

J'ai également participé à un webinaire CLIENT qui était destiné à présenter les fonctionnalités de Zeendoc et à discuter des avantages de l'intégration de l'API de validation des factures fournisseur. Cela m'a permis de mieux comprendre les besoins des clients et de voir comment Zeendoc est utilisé dans un environnement réel.

J'ai travaillé sur la création du cahier des charges pour la mise en place de l'API permettant de valider les factures fournisseurs automatiquement. J'ai étudié les besoins et les exigences du projet afin de définir les fonctionnalités et les spécifications nécessaires pour l'API.

La semaine s'est terminée par une réunion avec toute l'équipe pour faire un compte rendu de nos activités et discuter des prochaines étapes du projet.



### Semaine 2 (28/05 au 01/06):
Dans le cadre du développement du projet, j'ai configuré une WSL (Windows Subsystem for Linux) avec PHP, Apache et SOAP. Cela m'a permis de commencer à tester la connexion via SOAP sur PHP pour interagir avec Zeendoc.

J'ai également travaillé sur la création d'un export via fichier plat vers un objet PHP. Cela était nécessaire pour permettre la manipulation des données des factures fournisseurs dans le système et leur validation automatique.

Enfin, j'ai créé une interface provisoire pour permettre a un utilisateurs de tester la fonctionnalité de validation des factures fournisseurs avant la mise en place de l'API complète. Cette interface a servi de solution temporaire en attendant le déploiement final de l'API.

J'ai été confronté a plusieurs problèmes duent a la complexité du web service de Zeendoc. J'ai donc passé beaucoup de temps faire et refaire les mêmes fonctions pour pouvoir les tester et les améliorer. Lee web service de Zeendoc étant réservé aux clients, je n'ai pas pu trouver d'exemple de code pour m'aider à comprendre comment le web service fonctionne et la documentation est très limitée.