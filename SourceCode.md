# SourceCode


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
3. Create  autorun service.



#### Creating Service

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


