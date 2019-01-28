set -u

TMP_FILE=$(mktemp)

find $PWD/../../data/gapminder -type f -iname "*.cc.txt" -exec basename {} .cc.txt \; | sort > $TMP_FILE

if [[ $# -gt 0 ]]; then
	if grep -q -i "^$1" $TMP_FILE; then
		grep -i "^$1" $TMP_FILE | nl
	else
		echo "There are no countries starting with \""$1"\""
		exit 1
	fi

else
	grep -i "^[A-Z]" $TMP_FILE | nl
fi
