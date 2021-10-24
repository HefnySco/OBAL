#!/bin/bash



RED='\033[1;31m'
GREEN='\033[1;32m'
YELLOW='\033[1;33m'
BLUE='\033[1;34m'


NC='\033[0m' # No Color


echo -e $NC



echo -e $YELLOW "Select Ardupilot Services"
echo -e $GREEN
read -p "choose 1:plane 2:copter 3:rover 4:camera 5:Skip  "  vehicle

echo -e $NC
echo -e $GREEN "You chose: " $RED $vehicle $NC




case "$vehicle" in

1)  echo -e $YELLOW "select arduplane " $NC 
    vehicle="arduplane.service"
    ;;
2)  echo -e $YELLOW "select arducopter " $NC 
    vehicle="arducopter.service"
    ;;
3)  echo -e $YELLOW "select ardurover " $NC 
    vehicle="ardurover.service"
    ;;
4)  echo -e $YELLOW "select obal camera " $NC 
    vehicle="obal_camera.service"
    ;;
5)  echo  -e $GREEN "No Action ... Skipped" $NC 
    exit 0
    ;;
*) echo -e $RED "Bad Selection" $NC 
   exit -1
   ;;
esac

echo -e $GREEN
read -p "choose 1:Start 2:Stop 3:Restart 4:Enable 5:Disable 6:Skip  "  action
echo -e $NC

echo -e $GREEN "You chose: " $RED $action $NC


case "$action" in

1)  echo -e $YELLOW "Start" $NC 
    action="start"
    ;;
2)  echo -e $YELLOW "Stop" $NC 
    action="stop"
    ;;
3)  echo -e $YELLOW "Restart" $NC 
    action="restart"
    ;;
4)  echo  -e $GREEN "Enable" $NC 
    action="enable"
    ;;
5)  echo  -e $GREEN "Disable" $NC 
    action="disable"
    ;;
6)  echo  -e $GREEN "No Action ... Skipped" $NC 
    exit 0
    ;;
*) echo -e $RED "Bad Selection" $NC 
   exit -1
   ;;
esac


cmd="sudo systemctl $action $vehicle"
echo -e "$cmd"

$cmd



