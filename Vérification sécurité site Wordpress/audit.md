# audite de sécurité du site https://deltic.fr

## Sommaire

- [audite de sécurité du site https://deltic.fr](#audite-de-sécurité-du-site-httpsdelticfr)
  - [Sommaire](#sommaire)
  - [Présentation](#présentation)
  - [Outils utilisés](#outils-utilisés)
  - [resultat](#resultat)
    - [WPScan](#wpscan)
      - [installation](#installation)
      - [Utilisation](#utilisation)
      - [Résumé](#résumé)
        - [Détails des Plugins](#détails-des-plugins)
        - [Détails des Utilisateurs Identifiés](#détails-des-utilisateurs-identifiés)
    - [Nikto](#nikto)
      - [installation](#installation-1)
      - [Utilisation](#utilisation-1)
      - [Résumé](#résumé-1)
      - [Résumé de l'Analyse de Sécurité avec Nikto](#résumé-de-lanalyse-de-sécurité-avec-nikto)
    - [nmap](#nmap)
      - [installation](#installation-2)
      - [Utilisation](#utilisation-2)


## Présentation

Ce document est un audit de sécurité du site https://deltic.fr réalisé dans le cadre de l'alternance de Marius Hivelin chez Deltic.

## Outils utilisés

- WPScan

## resultat

### WPScan

#### installation

```bash
sudo apt install wpscan
```

#### Utilisation

```bash
wpscan --url https://deltic.fr/ --api-token XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```


#### Résumé

| Nom        | Résultat           | Statut                                                                  | Commentaire                                                                                                                        |
| ---------- | ------------------ | ----------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| Serveur    | Apache             | <span style="color:green">OK</span>                                     |                                                                                                                                    |
| PHP        | 7.4                | <span style="color:green">OK</span>                                     |                                                                                                                                    |
| WordPress  | 6.4.2              | <span style="color:green">OK</span>                                     |                                                                                                                                    |
| Thème      | Deltic             | <span style="color:green">OK</span>                                     |                                                                                                                                    |
| Plugins    | Détails ci-dessous | <span style="color:orange">A vérifier</span>                            | Voir détails                                                                                                                       |
| Robots.txt | Présent            | <span style="color:orange">A vérifier</span>                            | À examiner pour des directives de sécurité potentiellement manquantes ou mal configurées                                           |
| XML-RPC    | Activé             | <span style="color:red"><span style="color:red">Attention</span></span> | XML-RPC est activé, ce qui pourrait être une cible pour les attaques automatisées. À évaluer pour désactivation si non nécessaire. |

##### Détails des Plugins

| Nom du Plugin     | Version  | Statut                                         | Commentaire                                                   |
| ----------------- | -------- | ---------------------------------------------- | ------------------------------------------------------------- |
| contact-form-7    | 5.8.4    | <span style="color:red">À mettre à jour</span> | Version obsolète. Mettre à jour vers 5.8.5.                   |
| handl-utm-grabber | 2.7.26   | <span style="color:green">OK</span>            |                                                               |
| leadin            | 10.2.17  | <span style="color:green">OK</span>            |                                                               |
| obflink           | Inconnue | <span style="color:orange">Inconnu</span>      | À vérifier pour s'assurer de la sécurité et des mises à jour. |
| reviews-feed      | 1.1      | <span style="color:green">OK</span>            |                                                               |
| rocket-lazy-load  | 2.3.6    | <span style="color:green">OK</span>            |                                                               |
| wordpress-seo     | 21.7     | <span style="color:green">OK</span>            |                                                               |
| wpcf7-redirect    | 3.0.1    | <span style="color:red">À mettre à jour</span> | Version obsolète. Mettre à jour vers 3.1.2.                   |

##### Détails des Utilisateurs Identifiés

| Nom d'utilisateur   | Méthode de détection      | Commentaire                                  |
| ------------------- | ------------------------- | -------------------------------------------- |
| Mathieu Dumasdelage | Détecté via Rss Generator |                                              |
| Audrine Bodin       | Détecté via Rss Generator |                                              |
| kraken              | Détecté via Oembed API    | <span style="color:orange">A vérifier</span> |



### Nikto

#### installation

```bash
sudo apt install nikto
```

#### Utilisation

> commande de base
```bash
nikto -h https://deltic.fr/
```

> commande la plus complète
```bash
nikto -h https://deltic.fr/ -C all -T 123bde -F html -o results.html -evasion 1 -timeout 60 -useragent "MyNiktoScan" -Pause 500
```

* -h https://deltic.fr/ : l'adresse du site à auditer
* -C all : active toutes les vérifications
* -T 123bde : selectionne les tests à effectuer
  * 1 : test des fichiers/dociers intéressants
  * 2 : test des vulnérabilités de serveur
  * 3 : test d'injection 
  * b : test pour les bdd
  * d : test DoS
  * e : test execution
* -F html : format de sortie
* -evasion 1 :  contournement dispositif d'intrusion/pare-feu
* -timeout 60 : temps d'attente avant de considérer une requête comme échouée
* -useragent "MyNiktoScan" : nom de l'agent utilisateur
* -Pause 500 : temps d'attente entre chaque requête




#### Résumé

#### Résumé de l'Analyse de Sécurité avec Nikto

| Problème Identifié              | Détails                                                                                                              | Statut                                       | Recommandations                                                                                                        |
| ------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| Cookies sans drapeaux sécurisés | Plusieurs cookies sont créés sans les drapeaux `secure` et `httponly`.                                               | <span style="color:red">Attention</span>     | Configurez les cookies pour utiliser les drapeaux `Secure` et `HttpOnly`.                                              |
| En-têtes révélateurs            | En-têtes comme `x-powered-by: PHP/7.4` divulguent la technologie et la version utilisées.                            | <span style="color:red">Attention</span>     | Masquez ou supprimez ces en-têtes pour éviter de divulguer des détails sur les technologies du serveur.                |
| Adresse IP dans le cookie       | L'adresse IP est stockée dans le cookie `handl_ip`.                                                                  | <span style="color:red">Attention</span>     | Évaluez la nécessité de cette pratique et cessez de stocker les adresses IP dans les cookies si possible.              |
| Drupal Link Header              | Un en-tête de lien Drupal a été trouvé, inhabituel pour un site WordPress.                                           | <span style="color:red">Attention</span>     | Vérifiez pourquoi cet en-tête est présent et corrigez la configuration si nécessaire.                                  |
| X-Content-Type-Options manquant | L'en-tête n'est pas défini pour certains fichiers, permettant potentiellement au navigateur de changer le type MIME. | <span style="color:red">Attention</span>     | Ajoutez `X-Content-Type-Options: nosniff` aux réponses du serveur pour empêcher le navigateur de deviner le type MIME. |
| X-Redirect-By: WordPress        | Cet en-tête est utilisé par WordPress lors de redirections.                                                          | <span style="color:green">Information</span> | Bien que non critique, envisagez de masquer cet en-tête pour réduire les informations sur les technologies utilisées.  |



### nmap

#### installation

```bash
sudo apt install nmap
```

#### Utilisation

```bash
nmap -sV -sC -A -T4 -p- -oN nmap_scan.txt deltic.fr
```

* -sV : détermine les versions des services
* -sC : active les scripts par défaut
* -A : active la detection d'OS et de version
* -T4 : vitesse de scan
* -p- : scan tous les ports
* -oN nmap_scan.txt : enregistre les résultats dans un fichier
* deltic.fr : l'adresse du site à auditer
* 
