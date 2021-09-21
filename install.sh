if $USER != "root"
then
	echo "this script need to be launched as root"
else
	echo "Installing Python 3"
	apt install python3
	echo "copying rage-cli.py to /bin/ragecli"
	cp rage-cli.py /bin/ragecli
fi
