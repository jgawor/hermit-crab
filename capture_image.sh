#!/bin/bash

CUR_DIR="$(cd $(dirname $0) && pwd)"

IMAGE_DIR=$CUR_DIR/images

mkdir -p $IMAGE_DIR

TIMESTAMP=$(date +%Y%m%d-%H%M%S)
raspistill -w 1920 -h 1080 -o $IMAGE_DIR/$TIMESTAMP.jpg

ln -fs $IMAGE_DIR/$TIMESTAMP.jpg $CUR_DIR/web/latest-image.jpg
