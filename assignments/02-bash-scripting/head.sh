set -u

if [[ $# -eq 0 ]]; then
        echo "Usage: head.sh FILE"
                exit 1
fi

if [[ ! -f "$1" ]]; then
        echo "$1 is not a file"
	exit 1
fi

INPUT_FILE=$1
NUM_LINES=${2:-3}


i=0
while read -r LINE; do
        if [[ $i -lt  $NUM_LINES ]]; then
                i=$((i+1))
		echo $LINE
        else
		exit 0
        fi
done < "$INPUT_FILE"
