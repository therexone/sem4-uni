#!/bin/sh
echo 'Hi, What is your name? '
read name
echo "Hi  $name this is a bash script. Your system status is"
uname -a
echo "----------------------------"
echo "SYSTEM UPTIME:  $(uptime) "
echo "---------------------------"

echo "The current working directory is $(pwd)"
echo "--------------------------"

echo "The current processes running are "
ps -eo comm,pmem --sort -pmem
echo "--------------------"

echo "RAM STATUS"
echo "--------------------"
free -h
echo "\nExiting........."





