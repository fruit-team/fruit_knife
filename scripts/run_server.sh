#!/bin/bash
PORT_NUM=${1:-5000}
docker run -t -i -p ${PORT_NUM}:5000 -v `realpath ../src`:/root/src --rm fruit.team/fruit_knife:latest python /root/src/server.py
