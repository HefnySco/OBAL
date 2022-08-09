# SourceCode


[![How to Compile Ardupilot Software & Install it on Raspberry?](https://raw.githubusercontent.com/HefnySco/OBAL/main/images/youtube_how_to_Compile_AP_SW.png)](https://youtu.be/mYn49GbUL8Y "How to Compile Ardupilot Software & Install it on Raspberry?")


## Download 

Download Binaries from [here](https://firmware.ardupilot.org/).  Select vehicle type then search for OBAL. For obal copter [version 4.2.2 ](https://firmware.ardupilot.org/Copter/stable-4.2.2/obal/)

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
2. Create empty file /home/pi/ardu.parm using `touch /home/pi/ardu.parm` you can add any initialization parameters to this file. For example for Quadcopter X configuration:

create ardupilot.parm with the following data.

`SYSID_THISMAV    1`

`FRAME_CLASS 1`

`FRAME_TYPE  1`





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

Note: OBAL board default port is serial 0

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



## CPU Affinity
When running **RPI-4** or **RPI-Zero 2W **and using Camera or running other software with ardupilot, it is recommended to give ardupilot 1 or 2 dedicated CPUs to run on. This enhannce Ardupilot schedule timing as we are not running Linux-RT.

The below image shows cpu status using htop when cpu 3 & 4 are isolated using [isocpus](https://rt-labs.com/docs/p-net/prepare_raspberrypi.html#advanced-users-only-control-linux-real-time-properties "isocpus")=2,3


[![cpu-affinity](https://raw.githubusercontent.com/HefnySco/OBAL/main/images/cpu_affinity.png "cpu-affinity")](https://raw.githubusercontent.com/HefnySco/OBAL/main/images/cpu_affinity.png "cpu-affinity")

> yes values 2 & 3 are mapped to cpu 3 & 4yes values 2 & 3 are mapped to cpu 3 & 4


#### Steps for using CPU-Affinity Feature is easy.
First free one or more cpus in RPI by adding **isolcpus** to **/boot/cmdline.txt**
for example below is execution of 
```bash
cat /boot/cmdline.txt
```

```bash
console=tty1 root=PARTUUID=d9b3f436-02 rootfstype=ext4 elevator=deadline fsck.repair=yes rootwait modules-load=dwc2,g_ether quiet splash plymouth.ignore-serial-consoles isolcpus=2,3
```

**You need to reboot here.**

`sudo reboot now`

in Ardupilot you need to add parameter **-c**  or **--cpu-affinity**
for example:

```bash
/home/pi/ardurover -A  udp:**YourTargetIP**:14550:bcast -B /dev/serial0 -c 2,3
```



