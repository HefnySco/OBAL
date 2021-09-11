This board does not have any closed source or special drivers. Any Raspberry-Pi board will do the job. All you need is to compile Ardupilot from its main repository. It is straightforward.





    git clone https://github.com/ArduPilot/ardupilot.git
    cd ardupilot 
    make obal

For Raspberry-Zero you can download its cross-tool from [here](https://sourceforge.net/projects/raspberry-pi-cross-compilers/files/Raspberry%20Pi%20GCC%20Cross-Compiler%20Toolchains/Buster/GCC%2010.2.0/Raspberry%20Pi%201%2C%20Zero/)


you can compile using the following command


    ./waf configure --toolchain=/opt/cross-pi-gcc/bin/arm-linux-gnueabihf --board obal
    ./waf rover
    ./waf copter
    ./waf plane

