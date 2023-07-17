from dronekit import connect, VehicleMode
import time
connection_string="127.0.0.1:14550"
from pymavlink import mavutil
iha=connect(connection_string,wait_ready=True,timeout=100)
import math



def velocity(velocity_x, velocity_y,yaw_rate,velocity_z, iha):
	msg = iha.message_factory.set_position_target_local_ned_encode(
          0,
          0, 0,
          mavutil.mavlink.MAV_FRAME_BODY_OFFSET_NED, 
          0b0000011111000111,
          0, 0, 0, 
          velocity_x, velocity_y, velocity_z,
          0, 0, 0,
          0, math.radians(yaw_rate))

        iha.send_mavlink(msg)
        
        



velocity(5,0,0,0,iha)
print("x ekseninde ilerliyorum")
time.sleep(2)

velocity(0,5,0,0,iha)
print("y ekseninde ilerliyorum")
time.sleep(2)

velocity(0,0,0,-2,iha)
print("z ekseninde ilerliyorum")
time.sleep(2)

velocity(0,0,60,0,iha)
print("donuyorum")
time.sleep(2)
velocity(0,0,0,0,iha)
