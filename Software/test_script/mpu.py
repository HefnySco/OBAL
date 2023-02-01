import time
import spidev
import RPi.GPIO as GPIO

class MPU9250:
    __MPUREG_WHOAMI = 0x75
    __BMP_WHOAMI  = 0xD0
    __READ_FLAG   = 0x80
    __CS_0        = 8 
    __CS_1        = 7

    def __init__(self, spi_bus_number = 0, spi_dev_number = 1, spi_mode = 3):
        #GPIO.setwarnings(False)
        #GPIO.setmode(GPIO.BOARD)
        #GPIO.setup(self.__CS_0, GPIO.OUT, initial=0)
        #GPIO.setup(self.__CS_1, GPIO.OUT, initial=0)
        self.bus = spidev.SpiDev()
        self.spi_mode = spi_mode
        self.spi_bus_number = spi_bus_number
        self.spi_dev_number = spi_dev_number
        self.bus.open(self.spi_bus_number, self.spi_dev_number)
        self.bus.mode = self.spi_mode
        
    def WriteReg(self, reg_address, data, CS):
        GPIO.output(CS, GPIO.HIGH)
        tx = [reg_address, data]
        rx = self.bus.xfer2(tx)
        self.bus.close()
        GPIO.output(CS, GPIO.LOW)
        return rx

    def ReadReg(self, reg_address, CS, CS2):
        #GPIO.output(CS, GPIO.LOW)
        #GPIO.output(CS2, GPIO.HIGH)
        tx = [reg_address  | self.__READ_FLAG , 0x00]
        rx = self.bus.xfer2(tx)
        #GPIO.output(CS, GPIO.HIGH)
        #GPIO.output(CS2, GPIO.HIGH)
        return rx[1]

    def ReadRegs(self, reg_address, length, CS, CS2):
        GPIO.output(CS, GPIO.LOW)
        GPIO.output(CS2, GPIO.HIGH)
        tx = [0] * (length + 1)
        tx[0] = reg_address | self.__READ_FLAG
        rx = self.bus.xfer2(tx)
        GPIO.output(CS, GPIO.HIGH)
        GPIO.output(CS2, GPIO.HIGH)
        return rx[1:len(rx)]

    def testMPU(self):
        #response = self.ReadReg(self.__MPUREG_WHOAMI, MPU9250.__CS_0, MPU9250.__CS_1)
        response = self.ReadReg(self.__BMP_WHOAMI, MPU9250.__CS_1, MPU9250.__CS_0)
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


    