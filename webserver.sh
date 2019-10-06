#!/bin/bash

CUR_DIR="$(cd $(dirname $0) && pwd)"

mkdir -p $CUR_DIR/logs

python3 -u $CUR_DIR/webserver.py >> $CUR_DIR/logs/webserver.log 2>&1
