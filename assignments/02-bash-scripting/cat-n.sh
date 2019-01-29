#!/usr/bin/env bash

set -u

if [[ $# -eq 0 ]]; then
	echo "Usage: cat-n.sh FILE"
		exit 1
fi

if [[ ! -f "$1" ]]; then
	echo "$1 is not a file"
		exit 1	
fi

INPUT_FILE=$1

i=0
while read -r LINE; do
	i=$((i+1))
	#printf "%3d $LINE\n" $i
	echo "$i" "$LINE"
done < "$INPUT_FILE"

exit 0
