import time
import spidev
import RPi.GPIO as GPIO

class MPU9250:


	__MPUREG_WHOAMI = 0x75
	__READ_FLAG   = 0x80

	def __init__(self, spi_bus_number = 0, spi_dev_number = 1, spi_mode = 3):
        GPIO.setwarnings(False) 
        GPIO.setmode(GPIO.BOARD) 
        GPIO.setup(8,GPIO.OUT, initial=0)
        self.bus = spidev.SpiDev()
        self.bus.no_cs = False
        self.spi_mode = spi_mode
        self.spi_bus_number = spi_bus_number
        self.spi_dev_number = spi_dev_number

        
	def WriteReg(self, reg_address, data):
        GPIO.output(18, GPIO.HIGH)
        self.bus.open(self.spi_bus_number, self.spi_dev_number)
        self.bus.mode = self.spi_mode
        tx = [reg_address, data]
        rx = self.bus.xfer2(tx)
        self.bus.close()
        GPIO.output(18, GPIO.LOW)
        return rx

	def ReadReg(self, reg_address):
        GPIO.output(18, GPIO.HIGH)
        self.bus.open(self.spi_bus_number, self.spi_dev_number)
        self.bus.mode = self.spi_mode
        tx = [reg_address | self.__READ_FLAG, 0x00]
        rx = self.bus.xfer2(tx)
        self.bus.close()
        GPIO.output(18, GPIO.LOW)
        return rx[1]
        

	def ReadRegs(self, reg_address, length):
        self.bus.open(self.spi_bus_number, self.spi_dev_number)
        tx = [0] * (length + 1)
        tx[0] = reg_address | self.__READ_FLAG

        rx = self.bus.xfer2(tx)

        self.bus.close()
        return rx[1:len(rx)]
        
        
	def testMPU(self):
        response = self.ReadReg(self.__MPUREG_WHOAMI)
        print ("MPU Returned: {}".format(hex(response)))
        if (response == 0x71):
            return True
        else:
            return False



            
M = MPU9250(0,0)
if (M.testMPU()==True):
    print ("Found")
else:
    print ("Not Found")


