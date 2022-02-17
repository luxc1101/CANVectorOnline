from witmotion import IMU

def callback(msg):
    print(msg)

imu = IMU()
imu.subscribe(callback)