# Configuring Raspberry


## Raspberry Pi OS Lite (Legacy)

**IMPORTANT**
OBAL is tested on [Raspberry Pi OS Lite (Legacy)](https://www.raspberrypi.com/software/operating-systems/ "Raspberry Pi OS Lite (Legacy)"), you are welcome to try it on other versions and please share your experience.


## Enable SPI & I2C Buses

It is important to enable I2C & SPI Buses. These are two interfaces that are needed to communicate with sensors on the board.

To enable them you need to execute command.

`sudo raspi-config
`
An interface will appear like the image below, and you can easily go through it to enable I2C & SPI.

[![Interface Options](https://raw.githubusercontent.com/HefnySco/OBAL/main/images/rpi_config_interface_options.png "Enable SPI")](https://raw.githubusercontent.com/HefnySco/OBAL/main/images/rpi_config_interface_options.png "Interface Options")

[![Select SPI](https://raw.githubusercontent.com/HefnySco/OBAL/main/images/rpi_config_spi_options.png "Select SPI")](https://raw.githubusercontent.com/HefnySco/OBAL/main/images/rpi_config_spi_options.png "Select SPI")


[![Enable I2C](https://raw.githubusercontent.com/HefnySco/OBAL/main/images/rpi_config_spi_options_selected.png "Enable SPI")](https://raw.githubusercontent.com/HefnySco/OBAL/main/images/rpi_config_spi_options_selected.png "Enable SPI")


[![Enable I2C](https://raw.githubusercontent.com/HefnySco/OBAL/main/images/rpi_config_i2c_options_selected.png "Enable I2C")](https://raw.githubusercontent.com/HefnySco/OBAL/main/images/rpi_config_i2c_options_selected.png "Enable I2C")

You then need to reboot the board and login again.

`sudo reboot now
`

## Change I2C Bus Speed

Now you need to **enable I2C bus speed 400KHz**. This is a simple step. run command:

`sudo nano /boot/config.txt
`
and search for **dtparam=i2c_arm=on** and add  **,i2c_arm_baudrate=400000** next to it.
the result should be:

[![/boot/config.txt](https://raw.githubusercontent.com/HefnySco/OBAL/main/images/rpi_config_config.png "/boot/config.txt")](https://raw.githubusercontent.com/HefnySco/OBAL/main/images/rpi_config_config.png "/boot/config.txt")

**dtparam=i2c_arm=on,i2c_arm_baudrate=400000**
then press CTRL-X and save and exit.
you need to restart again

`sudo reboot now
`

