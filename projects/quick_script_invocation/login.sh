#!/bin/sh

for i in "$@"
do
case $i in 
  
  # Get the ip address
  -i=*|--ip=*)
  ip="${i#*=}"
  ;;
  
  # Get the user
  -u=*|--user=*)
  user="${i#*=}"
  ;;
  
  # Get the password
  -p=*|--password=*)
  password="${i#*=}"
  ;;
  
  
esac
done



# Execute sshpass command to access the host
sshpass -p "${password}" ssh ${user}@${ip}	 