#!/bin/bash

EMAIL=""

for mount in / /boot; do
    spaceUsed=$(df -H $mount | grep -v "Filesystem" | awk '{ print $5 }' | cut -d'%' -f1)
    echo "$mount is $spaceUsed% full."
    if [ "$spaceUsed" -ge 95 ]; then
	echo "Warning: $mount is $spaceUsed% full" | mail "$EMAIL"
    fi
done
