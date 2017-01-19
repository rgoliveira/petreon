<?php
// DIC configuration

$container = $app->getContainer();

// view renderer
$container['renderer'] = function ($c) {
    $settings = $c->get('settings')['renderer'];
    return new Slim\Views\PhpRenderer($settings['template_path']);
};

// monolog
$container['logger'] = function ($c) {
    $settings = $c->get('settings')['logger'];
    $logger = new Monolog\Logger($settings['name']);
    $logger->pushProcessor(new Monolog\Processor\UidProcessor());
    $logger->pushHandler(new Monolog\Handler\StreamHandler($settings['path'], $settings['level']));
    return $logger;
};

// db
$container['db'] = function ($c) {
    $settings = $c->get('settings')['db'];
    try {
        $connectionStr = "pgsql:host=" . $settings['host'] . ";port=" . $settings['port'] . ";dbname=" . $settings['dbname'] . ";user=" . $settings['user'] . ";password=" . $settings['password'];
        $c->logger->info($connectionStr);
        $pdo = new PDO($connectionStr);
    } catch (Exception  $e) {
        $c->logger->info($e->getMessage());
    }
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    $pdo->setAttribute(PDO::ATTR_DEFAULT_FETCH_MODE, PDO::FETCH_ASSOC);
    return $pdo;
};
