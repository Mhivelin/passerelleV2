<?php
require 'vendor/autoload.php';

// Ici on génère l'url pour l'identification et on redirige l'utilisateur vers celle-ci.
// https://developpeurs-storage.ebp.com/#authentification

$clientId = 'jupiterwithoutpkce'; // Client ID
//$redirectUriRaw = 'http://192.168.75.154/exportBAP/ebptest2.php'; // lien de redirection vers l'application
$redirectUriRaw = 'http://localhost:3333/oauth2_callback.php'; // lien de redirection vers l'application

$redirectUri = urlencode($redirectUriRaw); // On encode la redirectUri pour la passer dans l'url

$url = "https://api-login.ebp.com/connect/authorize/callback?client_id=" . $clientId .
    "&redirect_uri=" . $redirectUri .
    "&response_type=code&scope=openid%20profile%20offline_access&response_mode=query";

// Faire la requete vers l'authentification
header('Location: ' . $url);
exit();