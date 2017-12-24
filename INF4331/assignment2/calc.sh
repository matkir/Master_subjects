#!/bin/bash



maxnum () {
    if [ $2 -gt $1 ]
    then
        return $2
    else
        return $1
    fi
}

minnum () {
    if [ $2 -gt $1 ]
    then
        return $1
    else
        return $2
    fi
}



function plus {

a=$(( ${1} + ${2} ))
return $a
}


function stimes {

a=$(( ${1} * ${2} ))
return $a
}




#Assigning operaror
case $1 in 
	"S")
	operator=plus
	;;
	
	"P")
	operator=stimes
	;;
	"M")
	operator=maxnum
	;;
	"m")
	operator=minnum
	;;

	*)
	echo "Not a valid operator"
	exit 
esac
shift;
ret=$1
shift;

for i in $@; do
	eval $operator $ret $i
	ret=${?}
done	
echo $ret



