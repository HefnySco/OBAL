# Hardware Specification

#### Dimensions: 
49.91 mm x 100.2 mm



[![Obal2D](https://raw.githubusercontent.com/HefnySco/OBAL/main/images/Obal2D.png "pca9658")](https://raw.githubusercontent.com/HefnySco/OBAL/main/images/Obal2D.png "Obal2D")




#### IMU: IMU9250 - breakout GY-9250 via SPI

[![GY-9250](https://raw.githubusercontent.com/HefnySco/OBAL/main/images/sensors/9250_1.jpeg "GY-9250")](https://raw.githubusercontent.com/HefnySco/OBAL/main/images/sensors/9250_1.jpeg "GY-9250")

You can choose not to use this sensor and use wires to connect your sensors to SPI pins  on the board. 









#### Baro: BMP-180 via I2C

[![BMP-180](https://raw.githubusercontent.com/HefnySco/OBAL/main/images/sensors/baro180.png "BMP-180")](https://raw.githubusercontent.com/HefnySco/OBAL/main/images/sensors/baro180.png "BMP-180")



#### Current & Voltage Sensor: ADS1115 via I2C

[![ADS1115](https://raw.githubusercontent.com/HefnySco/OBAL/main/images/sensors/ADS1115.png "ADS1115")](https://raw.githubusercontent.com/HefnySco/OBAL/main/images/sensors/ADS1115.png "ADS1115")

The sensor has 4 sensing points. Only two is used to sens voltage and current as in APM & PIXHAWK. However this can be extended by software so that individual cells for 3S batteries are measured or to use the extra ADC pins in other functions.



#### PWM Output: PCA9685 via I2C

[![pca9658](https://raw.githubusercontent.com/HefnySco/OBAL/main/images/sensors/pca9658.png "pca9658")](https://raw.githubusercontent.com/HefnySco/OBAL/main/images/sensors/pca9658.png "pca9658")



This module can output PWM signals upto 16 channels.















####LED & Buzzer Driver: ULN2803APG

[![ULN2803APG_1](https://raw.githubusercontent.com/HefnySco/OBAL/main/images/sensors/ULN2803APG_1.png "ULN2803APG_1")](https://raw.githubusercontent.com/HefnySco/OBAL/main/images/sensors/ULN2803APG_1.png "ULN2803APG_1")

This IC is used to control LEDs & Buzzer. Each two outputs of the 8 outputs of the IC are wired up together so there are 4 output ports that support high current. OBAL uses only 2  leds not three and a buzzer. So there is an extra port that can be used.








#### Switch: 

This switch disables PWM output. It is not connected logically to Ardupilot. SO it is not the ARM switch of Ardupilot. It is a switch that disables PWM output by disabling PCA9685 using a chip enable pin.


#### Other Sensors:

All I2c & SPI sensors can be added easily to OBAL.

GPS can be connected to Serial-1 pins as they are connected to TX & RX of Raspberry-PI.

Telemetry can be connected via OTG in USB if you ar using Raspberry-Zero.
Other Raspberry-PI's already contain multiple USB and can accept multiple GPS & Telemetry.

