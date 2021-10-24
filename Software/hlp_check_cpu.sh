#!/bin/bash




RED='\033[1;31m'
GREEN='\033[1;32m'
YELLOW='\033[1;33m'
BLUE='\033[1;34m'


NC='\033[0m' # No Color


echo -e $NC



echo -e $YELLOW "Select Ardupilot Services to check"
echo -e $GREEN
read -p "choose 1:plane 2:copter 3:rover 4:Skip "  vehicle

echo -e $NC
echo -e $GREEN "You chose: " $RED $vehicle $NC




case "$vehicle" in

1)  echo -e $YELLOW "select arduplane " $NC 
    vehicle=arduplane
    ;;
2)  echo -e $YELLOW "select arducopter " $NC 
    vehicle=arducopter
    ;;
3)  echo -e $YELLOW "select ardurover " $NC 
    vehicle=ardurover
    ;;
4)  echo  -e $GREEN "No Action ... Skipped" $NC 
    exit 0
    ;;
*) echo -e $RED "Bad Selection" $NC 
   exit -1
   ;;
esac


sudo systemctl status --type service $vehicle.service

echo -e "On CPUs"
ps -mo pid,tid,%cpu,psr -C $vehicle



