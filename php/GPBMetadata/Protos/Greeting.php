<?php
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/greeting.proto

namespace GPBMetadata\Protos;

class Greeting
{
    public static $is_initialized = false;

    public static function initOnce() {
        $pool = \Google\Protobuf\Internal\DescriptorPool::getGeneratedPool();

        if (static::$is_initialized == true) {
          return;
        }
        $pool->internalAddGeneratedFile(
            '
?
protos/greeting.protogreeting"
HelloReq
name (	Rname"%
	HelloResp
message (	Rmessage2@
Greeter5
SayHello.greeting.HelloReq.greeting.HelloResp" bproto3'
        , true);

        static::$is_initialized = true;
    }
}

