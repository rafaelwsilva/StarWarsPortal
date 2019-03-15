<?php

ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

use App\Controllers\Drill;
require 'vendor/autoload.php';



// Create and configure Slim app
$config = ['settings' => [
    'addContentLengthHeader' => false,
]];
$app = new \Slim\App($config);



// Main Route
$app->get('/', function ($request, $response, $args) {
    return $response->withStatus(200)->write('<h1>Welcome to Star Wars Portal API!</h1>');
});

// Define app routes
$app->get('/chars', function ($request, $response, $args) {
    $drill = new Drill();
    $chars = $drill->getCharactersName();
    $return = $response->withJson($chars, 201)
        ->withHeader('Content-type', 'application/json');
    return $return;
});

// Define app routes
$app->get('/chars/{name}', function ($request, $response, $args) {
    $name = $args['name'];
    $drill = new Drill();
    $char = $drill->getCharByName($name);
    $return = $response->withJson($char, 201)
        ->withHeader('Content-type', 'application/json');
    return $return;

});


// Run app
$app->run();