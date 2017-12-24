#!/bin/bash


function func-add {
if [ ! -f $savefolder ]; then
    	echo "making .my_bookmark"
	echo -n > "$savefolder"
fi

combinedString=${1}"|"${currfolder}
echo $combinedString >> $savefolder
export ${1}=$PWD
}

function func-rem {
unset ${1}
sed -i '/^'${1}'/d'  $savefolder  

}


savefolder="$HOME/.my_bookmarks"
currfolder=$PWD

case $1 in 
	"-a")
	if [ "$#" -ne 2 ]; then
    		echo "Not enough input arguments:"
	fi
	func-add $2
	;; 
	
	"-r")
	if [ "$#" -ne 2 ]; then
    		echo "Not enough input arguments:"
	fi
	func-rem $2
	unset $2
	;;
	
	*)
	if [ "$#" -ne 0 ]; then
    		echo "Either wrong or missing arguments"
	fi

	while read NAME
	do
		A1=`echo $NAME | cut -d \| -f 1`
		A2=`echo $NAME | cut -d \| -f 2`
    		export $A1=$A2
	done < $savefolder	
	;;
esac
