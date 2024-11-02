import time
import board
import busio
from adafruit_lsm6ds.lsm6ds33 import LSM6DS33
from IMU import IMU

#unsure if this works yet, cannot test without actual IMU
i2c = busio.I2C(board.SCL, board.SDA)
sensor = LSM6DS33(i2c)

#assigns the class IMU to imu
imu = IMU

#calls classes definiton from IMU
imu.classes

#loop calling runLoop from IMU
while True:
    
    imu.runLoop
    
    time.sleep(0.5)