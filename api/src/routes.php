<?php
// Routes

function guidv4()
{
    $data = random_bytes(16);

    $data[6] = chr(ord($data[6]) & 0x0f | 0x40); // set version to 0100
    $data[8] = chr(ord($data[8]) & 0x3f | 0x80); // set bits 6-7 to 10

    return vsprintf('%s%s-%s-%s-%s-%s%s%s', str_split(bin2hex($data), 4));
};

$app->get('/campaign/[{uuid}]', function ($request, $response, $args) {
    $this->logger->info("GET /campaign");
    $stmt = $this->db->prepare("SELECT * FROM campaigns WHERE uuid = :uuid");
    $stmt->bindParam("uuid", $args["uuid"]);
    $stmt->execute();
    $campaign = $stmt->fetchObject();
    return $response->withJson($campaign);
});

$app->post('/campaign', function ($request, $response, $args) {
    $this->logger->info("POST /campaign");
    $input = $request->getParsedBody();
    $stmt = $this->db->prepare("INSERT INTO campaigns (uuid, name, description, age) VALUES (:uuid, :name, :description, :age)");
    $uuid = guidv4();
    $stmt->bindParam("uuid", $uuid);
    $stmt->bindParam("name", $input['name']);
    $stmt->bindParam("description", $input['description']);
    $stmt->bindParam("age", $input['age']);
    $stmt->execute();
    return $response->withJson($uuid);
});

$app->delete('/campaign/[{uuid}]', function ($request, $response, $args) {
    $this->logger->info("POST /campaign");
    $stmt = $this->db->prepare("DELETE FROM campaigns WHERE uuid = :uuid");
    $stmt->bindParam("uuid", $args['uuid']);
    $stmt->execute();
    return $response->withJson($args['uuid']);
});

$app->get('/campaigns', function ($request, $response, $args) {
    $this->logger->info("GET /campaigns");
    $stmt = $this->db->prepare("SELECT * FROM campaigns");
    $stmt->execute();
    $campaigns = $stmt->fetchAll();
    return $response->withJson($campaigns);
});

$app->get('/', function ($request, $response, $args) {
    // Sample log message
    $this->logger->info("Slim-Skeleton '/' route");

    // Render index view
    return $response->getBody()->write("Hello Petreon");
});

$app->get('/test', function ($request, $response, $args) {
    return $response->getBody()->write("Hello test");
});

