#! /bin/bash
echo -en "\ec"

case $1 in
	"no")
	TZ='Europe/Oslo' ; export TZ
	;;

	"us")
	TZ='America/New_York' ; export TZ
	;;

	"sk")
	TZ='Asia/Seoul' ; export TZ
	;;
	
esac
while true
do 
	date +"%R:%S"
	sleep 1s
	echo -en "\ec"
done
