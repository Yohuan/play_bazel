#!/bin/bash
set -e
cd $(dirname $0)

php -d extension=grpc.so -d max_execution_time=300 greeting_client.php $1
