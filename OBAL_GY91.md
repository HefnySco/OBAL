# OBAL-GY91 ver 1.0

[![Obal-GY-91 Board 3D](https://raw.githubusercontent.com/HefnySco/OBAL/main/images/img_OBAL_GY_91.png "Obal-GY-91 Board 3D")](https://raw.githubusercontent.com/HefnySco/OBAL/main/images/img_OBAL_GY_91.png "Obal-GY-91 Board 3D")


This board is very similar to the original one. I have replaced MPU-9250 & BMP180 with [GY-91](https://www.aliexpress.com/item/1005001636248651.html?spm=a2g0o.productlist.0.0.38b47172eQlyss&algo_pvid=3cafb618-f428-4e50-84b9-fc538d546b24&algo_exp_id=3cafb618-f428-4e50-84b9-fc538d546b24-1&pdp_ext_f=%7B%22sku_id%22%3A%2212000016917052419%22%7D&pdp_pi=-1%3B6.84%3B-1%3B368%40salePrice%3BUSD%3Bsearch-mainSearch) that contains MPU-9250 & BMP280 on one breakout. 


This slight modification reduces space occupied by the sensors and reduce number of sensors accessed by I2C.

[![GY-91](https://raw.githubusercontent.com/HefnySco/OBAL/main/images/sensors/gy_91.jpeg "GY-91")](https://raw.githubusercontent.com/HefnySco/OBAL/main/images/sensors/gy_91.jpeg "GY-91")


The overall performance is much the same as original OBAL. The whole point is now you can add extra BMP180 without I2C address conflict.


If you already have the original OBAL board you can still use this sensor on it. But in this case you need to wire it externally. You will need to use CS1 of SPI1 as well. It is already available. Because OBAL is more like LEGO you can use any board with any sensor.

[![Original OBAL with GY-91](https://raw.githubusercontent.com/HefnySco/OBAL/main/images/obal_org_w_gy91.png "Original OBAL with GY-91")](https://raw.githubusercontent.com/HefnySco/OBAL/main/images/obal_org_w_gy91.png "Original OBAL with GY-91")



The software installation and other sensors and wiring are all identical. There is no any change. However you need to compile Ardupilot to recognize the new sensors. That is why I created a new branch [![here](https://github.com/HefnySco/ardupilot/tree/pr_OBAL_GY-91_v1 "here")]. Changes are limited to two files. if you are familiar with git you can edit them manually into the master code or Ardupilot.

Please note that original OBAL is part of Ardupilot master code as well as release version for Copter & Plane. So you can download the latest version of the source code from Ardupilot and apply these slight changes and that is it.






