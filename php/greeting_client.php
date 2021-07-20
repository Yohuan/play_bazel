<?php

require dirname(__FILE__).'/vendor/autoload.php';

function greet($hostname, $name)
{
    $client = new Greeting\GreeterClient($hostname, [
        'credentials' => Grpc\ChannelCredentials::createInsecure(),
    ]);
    $request = new Greeting\HelloReq();
    $request->setName($name);
    list($response, $status) = $client->SayHello($request)->wait();
    if ($status->code !== Grpc\STATUS_OK) {
        echo "ERROR: " . $status->code . ", " . $status->details . PHP_EOL;
        exit(1);
    }
    echo $response->getMessage() . PHP_EOL;
}

$name = empty($argv[1]) ? 'world': $argv[1];
$hostname = 'localhost:5566';
greet($hostname, $name);
