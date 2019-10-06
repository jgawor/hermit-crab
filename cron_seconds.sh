#!/bin/bash

CRON_SECONDS=$1
shift

TRIES=$(expr 60 / $CRON_SECONDS)

"$@"
for (( c=1; c<$TRIES; c++ )); do
    sleep $CRON_SECONDS
    "$@"
done
