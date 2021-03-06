<?php
// GENERATED CODE -- DO NOT EDIT!

namespace Greeting;

/**
 */
class GreeterClient extends \Grpc\BaseStub {

    /**
     * @param string $hostname hostname
     * @param array $opts channel options
     * @param \Grpc\Channel $channel (optional) re-use channel object
     */
    public function __construct($hostname, $opts, $channel = null) {
        parent::__construct($hostname, $opts, $channel);
    }

    /**
     * @param \Greeting\HelloReq $argument input argument
     * @param array $metadata metadata
     * @param array $options call options
     * @return \Grpc\UnaryCall
     */
    public function SayHello(\Greeting\HelloReq $argument,
      $metadata = [], $options = []) {
        return $this->_simpleRequest('/greeting.Greeter/SayHello',
        $argument,
        ['\Greeting\HelloResp', 'decode'],
        $metadata, $options);
    }

}
