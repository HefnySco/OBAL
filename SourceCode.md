# SourceCode


[![How to Compile Ardupilot Software & Install it on Raspberry?](https://raw.githubusercontent.com/HefnySco/OBAL/main/images/youtube_how_to_Compile_AP_SW.png)](https://youtu.be/mYn49GbUL8Y "How to Compile Ardupilot Software & Install it on Raspberry?")


## Download 

Download Binaries from [here](https://drive.google.com/drive/folders/1e5yGQsX_wOOnu_0mpdkT8hTYvYcqudqF?usp=sharing). You can find different folders for different boards and configuration.

## Building The Code

This board does not have any closed source or special drivers. Any Raspberry-Pi board will do the job. All you need is to compile Ardupilot from its main repository. It is straightforward.





    git clone https://github.com/ArduPilot/ardupilot.git
    cd ardupilot 
    git submodule update --init  --recursive
    make obal

For Raspberry-Zero you can download its cross-tool from [here](https://sourceforge.net/projects/raspberry-pi-cross-compilers/files/Raspberry%20Pi%20GCC%20Cross-Compiler%20Toolchains/Buster/GCC%2010.2.0/Raspberry%20Pi%201%2C%20Zero/)


you can compile using the following command


    ./waf configure --toolchain=/opt/cross-pi-gcc/bin/arm-linux-gnueabihf --board obal
    ./waf rover
    ./waf copter
    ./waf plane




## Deploy Binary

1. Copy ardupilot binary to /home/pi .
2. Create empty file /home/pi/ardu.parm using touch /home/pi/ardu.parm you can add any initialization parameters to this file.




## Run ArduPilot

ArduCopter:
`sudo /home/pi/arducopter` (plus parameter) 

ArduPlane:
`sudo /home/pi/arduplane` (plus parameter) 

ArduRover:
`sudo /home/pi/ardurover` (plus parameter) 

ArduSub:
`sudo /home/pi/ardusub` (plus parameter) 


Start Parameter | ArduPilot Serial Port 
------------ | -------------
-A | SERIAL0
-B | SERIAL3
-C | SERIAL1
-D | SERIAL2
-E | SERIAL4
-F | SERIAL5

Check http://ardupilot.org/copter/docs/parameters.html#serial0-baud-serial0-baud-rate to set the right value for `SERIALx_BAUD` and `SERIALx_PROTOCOL`

To connect a MAVLink groundstation with IP 192.168.1.123 add `-C udp:192.168.1.123:14550`

To use MAVLink via radio connected to Serial0 add `-C /dev/serial0`. 

If there is a GPS connected to Serial1 add `-B /dev/serial1`. 

Example: MAVLink groundstation with IP 192.168.178.26 on port 14550 via wifi and GPS connected to `/dev/serial0` and telemetry via OTG `/dev/serial1`.

`sudo /home/pi/arducopter -A udp:192.168.1.123:14550 -B /dev/serial0 -C serial1`



## Running as a Service

create service file and edit it

`sudo nano /lib/systemd/system/ardurover.service
`



```bash
[Unit]
Description=ArduPilot-Rover for Linux OPAL Board
After=systemd-modules-load.service
Documentation=https://docs.obal.com/page.html
Conflicts=arduplane.service arducopter.service ardurover.service

[Service]
Type=single
ExecStart=/home/pi/ardurover -A  udp:**YourTargetIP**:14550:bcast -B /dev/serial0
Restart=on-failure

[Install]
WantedBy=multi-user.target

```

Above file is for running rover but you can replace ardurover with other binaries e.g. arducopter & arduplane.


## Running Service

`sudo systemctl enable ardurover.service
`
  
`sudo systemctl start ardurover.service
`



