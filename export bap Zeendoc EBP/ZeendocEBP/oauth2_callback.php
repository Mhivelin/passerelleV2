<?php

require 'vendor/autoload.php';

if (!isset($_GET['code'])) {
    throw new Exception('Code is not defined');
}

use GuzzleHttp\Client;

// On récupère le code retourné par EBP
$code = $_GET['code'];

/**
 * Récupérer le token
 *
 * @param string $code
 * @return string Token
 */
function GetToken($code) {
    $clientId = 'jupiterwithoutpkce'; // Client ID
    $clientSecret = '78f68eac-c4e2-4221-9836-d66db48a75f0'; // Client Secret
    $redirectUri = 'http://localhost:3333/oauth2_callback.php'; // lien de redirection vers l'application

    $bytes = random_bytes(32);
    $codeVerifier = rtrim(strtr(base64_encode($bytes), '+/', '-_'), '=');

    $client_o2 = new Client([
        // Base URI is used with relative requests
        'base_uri' => 'https://api-login.ebp.com'
    ]);

    $data_o2 = [
        'client_id' => $clientId,
        'client_secret' => $clientSecret,
        'grant_type' => 'authorization_code',
        'code' => $code,
        'code_verifier' => $codeVerifier,
        'redirect_uri' => $redirectUri
    ];

    $response_o2 = $client_o2->post('/connect/token', $data_o2);

    return $response_o2['access_token'];
}

/**
 * Faire une requête sur l'API
 *
 * @param string $token Token
 * @param string $endpoint Route de la requête
 */
function MakeApiCall($token, $endpoint) {
    $subscriptionKey = 'ded59b2d14d44e24b6bd1ae64ca45d6d'; // Subscription Key

    $client = new Client([
        // Base URI is used with relative requests
        'base_uri' => 'https://api-developpeurs.ebp.com'
    ]);

    return $client->get($endpoint, [
        'headers' => [
            'Authorization' => 'Bearer ' . $token,
            'ebp-subscription-key' => $subscriptionKey
        ]
    ]);
}

$token = GetToken($code);
$response = MakeApiCall($token, "/gescom/api/v1/Folders");

echo $response;