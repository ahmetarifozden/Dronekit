from dronekit import connect, VehicleMode
import time
connection_string="127.0.0.1:14550"
from pymavlink import mavutil
iha=connect(connection_string,wait_ready=True,timeout=100)
import math

def arm_ol_ve_yuksel(hedef_yukseklik):
	while iha.is_armable==False:
		print("Arm ici gerekli sartlar saglanamadi.")
		time.sleep(1)
	print("Iha su anda armedilebilir")
	
	iha.mode=VehicleMode("GUIDED")
	while iha.mode!='GUIDED':
		print('Guided moduna gecis yapiliyor')
		time.sleep(1.5)

	print("Guided moduna gecis yapildi")
	iha.armed=True
	while iha.armed is False:
		print("Arm icin bekleniliyor")
		time.sleep(1)

	print("Ihamiz arm olmustur")
	
	iha.simple_takeoff(hedef_yukseklik)
	while iha.location.global_relative_frame.alt<=hedef_yukseklik*0.94:
		print("Su anki yukseklik{}".format(iha.location.global_relative_frame.alt))
		time.sleep(0.5)
	print("Takeoff gerceklesti")
	
def pozisyon(posx, posy,yaw_rate,posz, iha):
	msg = iha.message_factory.set_position_target_local_ned_encode(
          0,
          0, 0,
          mavutil.mavlink.MAV_FRAME_LOCAL_NED, 
          0b0000011111111000,
          posx, posy, posz, #pozisyonlar(metre)
          0, 0, 0,#hizlar(metre/s)
          0, 0, 0,#akselarasyon(fonksiyonsuz)
          0, math.radians(yaw_rate))#yaw,yaw_rate(rad,rad/s)

        iha.send_mavlink(msg)
        

def velocity(velocity_x, velocity_y,yaw_rate,velocity_z, iha):
	msg = iha.message_factory.set_position_target_local_ned_encode(
          0,
          0, 0,
          mavutil.mavlink.MAV_FRAME_BODY_OFFSET_NED, 
          0b0000011111000111,
          0, 0, 0,  #pozisyonlar(metre)
          velocity_x, velocity_y, velocity_z, #hizlar(metre/s)
          0, 0, 0, #akselarasyon(fonksiyonsuz)
          0, math.radians(yaw_rate))#yaw,yaw_rate(rad,rad/s)

        iha.send_mavlink(msg)        
        
        
        
        
arm_ol_ve_yuksel(15);

pozisyon(40,0,0,-15,iha)
while iha.location.local_frame.north<=39.90
	print("40 metre kuzeye ilerliyorum")
	time.sleep
print("kuzeydeyim")	
	
velocity(0,0,90,0,iha)
print("donuyorum")
time.sleep(2)

pozisyon(40,30,0,-15,iha)
while iha.location.local_frame.north<=29.90
	print("30 metre doğuya ilerliyorum")
	time.sleep
print("doğudayım")	

velocity(0,0,90,0,iha)
print("donuyorum")
time.sleep(2)

pozisyon(-40,30,0,-15,iha)
while iha.location.local_frame.north<=39.90
	print("80 metre güneye ilerliyorum")
	time.sleep
print("güneydeyim")	


velocity(0,0,90,0,iha)
print("donuyorum")
time.sleep(2)


pozisyon(-40,0,0,-15,iha)
while iha.location.local_frame.north<=39.90
	print("80 metre batıya ilerliyorum")
	time.sleep
print("batıdayım")	


velocity(0,0,90,0,iha)
print("donuyorum")
time.sleep(2)

	
pozisyon(0,0,0,-15,iha)
while iha.location.local_frame.north<=39.90
	print("80 metre batıya ilerliyorum")
	time.sleep
print("batıdayım")
