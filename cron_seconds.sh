#!/bin/bash

SECONDS=$1
shift

TRIES=$(expr 60 / $SECONDS)

"$@"
for (( c=1; c<$TRIES; c++ )); do
    sleep $SECONDS
    "$@"
done
