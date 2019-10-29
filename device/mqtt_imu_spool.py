import halo
import time
import event


# *** CONSTANTS *** -----------------------------------------------------
#
# wifi info
SSID                   = 'EasyBox-114895'
SSPWD                  = '784SuPeR!?364'
WIFI_NOT_CONNECTED_MSG = "WIFI not connected"

# mqtt info
MQTT_TOPIC      = '/KLEINHOLDERMANN/HALOCODE'
MQTT_SERVER     = "test.mosquitto.org"

# IMU info
IMU_SAMPLE_FREQUENCY = 50 # Hz
IMU_SAMPLE_DURATION  =  1 # s

# other
START_RING_DURATION = 6 # seconds


# *** INIT *** -----------------------------------------------------

# init mqtt channel
halo.cloud_message.start(MQTT_TOPIC, client_id = None, server = MQTT_SERVER)


# init wifi
halo.wifi.start(ssid = SSID, password = SSPWD, mode = halo.wifi.WLAN_MODE_STA)
while not halo.wifi.is_connected():
     print(WIFI_NOT_CONNECTED_MSG)
     time.sleep(2)

halo.led.show_all(126, 211, 33)
time.sleep(2)
halo.led.off_all()

# reset rotation angles
halo.motion_sensor.reset_rotation(axis = "all")


# *** FUNC *** -----------------------------------------------------

def led_start_sequence():
     for i in range(1,13): 
         halo.led.show_single(i, 0, 255, 0)
         time.sleep(1 / START_RING_DURATION)
     halo.led.show_all(255, 0, 0)

def imu_sample_data():
     rx, ry, rz, ax, ay, az  = [], [], [], [], [], []
     t = 0
     while t <= IMU_SAMPLE_DURATION:
         rx.append(halo.motion_sensor.get_rotation("x"))
         ry.append(halo.motion_sensor.get_rotation("y"))
         rz.append(halo.motion_sensor.get_rotation("z"))
         ax.append(halo.motion_sensor.get_acceleration("x"))
         ay.append(halo.motion_sensor.get_acceleration("y"))
         az.append(halo.motion_sensor.get_acceleration("z"))
         time.sleep(1 / IMU_SAMPLE_FREQUENCY)
         t = t + 1 / IMU_SAMPLE_FREQUENCY

     return rx, ry, rz, ax, ay, az

def wifi_spool_data(rx, ry, rz, ax, ay, az):
     halo.cloud_message.broadcast(str(rx), "rotation x "     + str(IMU_SAMPLE_FREQUENCY) + " Hz")
     halo.cloud_message.broadcast(str(ry), "rotation y "     + str(IMU_SAMPLE_FREQUENCY) + " Hz")
     halo.cloud_message.broadcast(str(rz), "rotation z "     + str(IMU_SAMPLE_FREQUENCY) + " Hz")
     halo.cloud_message.broadcast(str(ax), "acceleration x " + str(IMU_SAMPLE_FREQUENCY) + " Hz")
     halo.cloud_message.broadcast(str(ay), "acceleration y " + str(IMU_SAMPLE_FREQUENCY) + " Hz")
     halo.cloud_message.broadcast(str(az), "acceleration z " + str(IMU_SAMPLE_FREQUENCY) + " Hz")
    

# *** MAIN *** -----------------------------------------------------

while True:
     if halo.button.is_pressed():
         led_start_sequence()
         rx, ry, rz, ax, ay, az = imu_sample_data()
         halo.led.show_all(0, 0, 255)
         wifi_spool_data(rx, ry, rz, ax, ay, az)
         halo.led.off_all()
