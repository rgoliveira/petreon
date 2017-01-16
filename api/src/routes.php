<?php
// Routes

$app->get('/', function ($request, $response, $args) {
    // Sample log message
    $this->logger->info("Slim-Skeleton '/' route");

    // Render index view
    return $response->getBody()->write("Hello Petreon");
});

$app->get('/test', function ($request, $response, $args) {
    return $response->getBody()->write("Hello test");
});
