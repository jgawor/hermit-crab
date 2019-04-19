#!/bin/bash -e

CUR_DIR="$(cd $(dirname $0) && pwd)"

IMAGE_DIR=$CUR_DIR/images
VIDEO_DIR=$CUR_DIR/videos

mkdir -p $IMAGE_DIR
mkdir -p $VIDEO_DIR

TIMESTAMP=$(date +%Y%m%d-%H%M%S)

cd $IMAGE_DIR
ls -1 *.jpg | sort | awk '{ print "file", $1 }' > image.list

ffmpeg -r 5 -f concat -i "image.list" -vcodec libx264 $VIDEO_DIR/$TIMESTAMP.mp4

cat image.list  | sed 's/file//' | xargs rm -v

$CUR_DIR/google_drive_upload.py $VIDEO_DIR/$TIMESTAMP.mp4
