#132tpg256.py
#Read set point value at the start
#Read pressure every ~1 sec

import serial, string
from time import sleep

from epics import caput, caget
#ser.close()
#ser = serial.Serial('COM24', timeout=2, baudrate=9600, bytesize=8, parity='N', stopbits=1, xonxoff=0, rtscts=0)

print("APX Maxigauge")
while True:
	ser = serial.Serial('COM24', timeout=2, baudrate=9600, bytesize=8, parity='N', stopbits=1, xonxoff=0, rtscts=0)    
	#Set point status
	ser.write("SPS\r\n".encode())
	sleep(0.1)
	out = ''
	out = ser.read(ser.inWaiting())
	ser.write(b'\x05')
	sleep(0.1)
	out = ''
	out = ser.read(ser.inWaiting())
	#    print("BL132:132WRG1STS",out.decode().rstrip().split(',')[0])
	APXSP_A=out.decode().rstrip().split(',')[0]
	APXSP_B=out.decode().rstrip().split(',')[1]
	APXSP_C=out.decode().rstrip().split(',')[2]
	APXSP_D=out.decode().rstrip().split(',')[3]
	APXSP_E=out.decode().rstrip().split(',')[4]
	APXSP_F=out.decode().rstrip().split(',')[5]
    	#print(BL132_132PG1,end='\r')
	sleep(0.1)

	caput('APX:SP_SES100',APXSP_E)
	#Read Pressure

	ser.write("PR1\r\n".encode())
	sleep(0.1)
	out = ''
	out = ser.read(ser.inWaiting())
	ser.write(b'\x05')
	sleep(0.1)
	out = ''
	out = ser.read(ser.inWaiting())
	APXHPC100STS=out.decode().rstrip().split(',')[0]
	APXHPC100=out.decode().rstrip().split(',')[1]
	caput('APX:HPC100',APXHPC100)
	sleep(0.1)

	ser.write("PR2\r\n".encode())
	sleep(0.1)
	out = ''
	out = ser.read(ser.inWaiting())
	ser.write(b'\x05')
	sleep(0.1)
	out = ''
	out = ser.read(ser.inWaiting())
	APXHPCSTS=out.decode().rstrip().split(',')[0]
	APXHPC=out.decode().rstrip().split(',')[1]
	caput('APX:HPC',APXHPC)
	sleep(0.1)

	ser.write("PR3\r\n".encode())
	sleep(0.1)
	out = ''
	out = ser.read(ser.inWaiting())
	ser.write(b'\x05')
	sleep(0.1)
	out = ''
	out = ser.read(ser.inWaiting())
	APXPREPSTS=out.decode().rstrip().split(',')[0]
	APXPREP=out.decode().rstrip().split(',')[1]
	caput('APX:PREP',APXPREP)
	sleep(0.1)

	ser.write("PR4\r\n".encode())
	sleep(0.1)
	out = ''
	out = ser.read(ser.inWaiting())
	ser.write(b'\x05')
	sleep(0.1)
	out = ''
	out = ser.read(ser.inWaiting())
	APXAP1STS=out.decode().rstrip().split(',')[0]
	APXAP1=out.decode().rstrip().split(',')[1]
	caput('APX:AP1',APXAP1)
	sleep(0.1)

	ser.write("PR5\r\n".encode())
	sleep(0.1)
	out = ''
	out = ser.read(ser.inWaiting())
	ser.write(b'\x05')
	sleep(0.1)
	out = ''
	out = ser.read(ser.inWaiting())
	APXAP2STS=out.decode().rstrip().split(',')[0]
	APXAP2=out.decode().rstrip().split(',')[1]
	caput('APX:AP2',APXAP2)
	sleep(0.1)

	ser.write("PR6\r\n".encode())
	sleep(0.1)
	out = ''
	out = ser.read(ser.inWaiting())
	ser.write(b'\x05')
	sleep(0.1)
	out = ''
	out = ser.read(ser.inWaiting())
	APXHPC01STS=out.decode().rstrip().split(',')[0]
	APXHPC01=out.decode().rstrip().split(',')[1]
	caput('APX:HPC01',APXHPC01)
	sleep(0.1)

	print("SP",APXSP_E,"SEN",APXHPC100STS,APXHPC100,APXHPCSTS,APXHPC,APXPREPSTS,APXPREP,APXAP1STS,APXAP1,APXAP2STS,APXAP2,APXHPC01STS,APXHPC01,end='\r')
	#print("SP[A-F]",APXSP_A,APXSP_B,APXSP_C,APXSP_D,APXSP_E,APXSP_F,end='\r')






	SENCMD='SEN,'
	SENCMD_FLAG=0
	#if caget('APX:SEN1_OFF')==1:
	#	SENCMD=SENCMD+'1,'
	#	SENCMD_FLAG=1
	#	caput('APX:SEN1_OFF',0)
	#elif caget('APX:SEN1_ON')==1:
	#	SENCMD=SENCMD+'2,'
	#	SENCMD_FLAG=1
	#	caput('APX:SEN1_ON',0)
	#else:
	#	SENCMD_FLAG=0
	SENCMD=SENCMD+'0,'
	if caget('APX:SEN2_OFF')==1:
		SENCMD=SENCMD+'1,'
		SENCMD_FLAG=1
		caput('APX:SEN2_OFF',0)
	elif caget('APX:SEN2_ON')==1:
		SENCMD=SENCMD+'2,'
		SENCMD_FLAG=1
		caput('APX:SEN2_ON',0)
	else:
		SENCMD=SENCMD+'0,'
		#SENCMD_FLAG=0
	if caget('APX:SEN3_OFF')==1:
		SENCMD=SENCMD+'1,'
		SENCMD_FLAG=1
		caput('APX:SEN3_OFF',0)
	elif caget('APX:SEN3_ON')==1:
		SENCMD=SENCMD+'2,'
		SENCMD_FLAG=1
		caput('APX:SEN3_ON',0)
	else:
		SENCMD=SENCMD+'0,'
		#SENCMD_FLAG=0
	if caget('APX:SEN4_OFF')==1:
		SENCMD=SENCMD+'1,'
		SENCMD_FLAG=1
		caput('APX:SEN4_OFF',0)
	elif caget('APX:SEN4_ON')==1:
		SENCMD=SENCMD+'2,'
		SENCMD_FLAG=1
		caput('APX:SEN4_ON',0)
	else:
		SENCMD=SENCMD+'0,'
		#SENCMD_FLAG=0
	if caget('APX:SEN5_OFF')==1:
		SENCMD=SENCMD+'1,'
		SENCMD_FLAG=1
		caput('APX:SEN5_OFF',0)
	elif caget('APX:SEN5_ON')==1:
		SENCMD=SENCMD+'2,'
		SENCMD_FLAG=1
		caput('APX:SEN5_ON',0)
	else:
		SENCMD=SENCMD+'0,'
		#SENCMD_FLAG=0
	#if caget('APX:SEN6_OFF')==1:
	#	SENCMD=SENCMD+'1,'
	#	SENCMD_FLAG=1
	#	caput('APX:SEN6_OFF',0)
	#elif caget('APX:SEN6_ON")==1:
	#	SENCMD=SENCMD+'2,'
	#	SENCMD_FLAG=1
	#	caput('APX:SEN6_ON',0)
	#else:
	#	SENCMD_FLAG=0
	SENCMD=SENCMD+'0,'
	SENCMD=SENCMD+'\r\n'
	if SENCMD_FLAG==1:
		print(SENCMD)
		ser.write(SENCMD.encode())
		sleep(0.2)
		out = ''
		out = ser.read(ser.inWaiting())
		ser.write(b'\x05')
		sleep(0.3)
		out = ''
		out = ser.read(ser.inWaiting())

	ser.close()