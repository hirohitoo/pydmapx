#import pprint
#import nidaqmx
#import statistics
import time

from epics import caput,caget

list = ["APX:V0_","APX:V1_","APX:V2_","APX:V3_","APX:V4_","APX:V5_","APX:V6_","APX:V7_"]
list1= ["OPEN_REQ","OPEN_ENB","CLOSE_REQ"]
print("132valvecontrol.py")
actionlist=[]
openreqlist=[]
openenblist=[]
closereqlist=[]
#k=0
for i in list:
	#for j in list1:	
	#	print(i+j,bool(int(caget(i+j))))
		#print('\t')
	#print('\n')
	actionlist.append(bool(int(caget(i+"OPEN_ACT"))))
	openreqlist.append(bool(int(caget(i+"OPEN_REQ"))))
	openenblist.append(bool(int(caget(i+"OPEN_ENB"))))
	closereqlist.append(bool(int(caget(i+"CLOSE_REQ"))))
	#k=k+1

print(''.join(str(actionlist)))
print(''.join(str(openreqlist)))
print(''.join(str(openenblist)))
print(''.join(str(closereqlist)))

#print(caget("BL132:Iz"))  
#print(caget("BL132:Io"))
#print(caget("BL132:Id"))
#print(caget("BL132:Is"))
#print(caget("BL132:m1yaw_2_LVDT"))
#print(caget("BL132:m2pit_2_LVDT"))
#print("132valvecontrol.py")
#print("          ","APX:V0_","APX:V1_","APX:V2_","APX:V3_","APX:V4_","APX:V5_","APX:V6_","APX:V7_")
#print("OPEN_ACT  ")
#print("OPEN_REQ  ")
#print("OPEN_ENB  ")
#print("CLOSE_REQ ")

while True:
#    with nidaqmx.Task() as task0:
#        task0.di_channels.add_di_chan("cDAQ2Mod4/port0/line0:1", line_grouping=LineGrouping.CHAN_PER_LINE) 
#        data0=task0.read(number_of_samples_per_channel=1)   
    
#    with nidaqmx.Task() as task1:
#        task1.di_channels.add_di_chan("cDAQ2Mod4/port0/line0:1", line_grouping=LineGrouping.CHAN_PER_LINE) 
#        data1=task1.read(number_of_samples_per_channel=1)
    
#    with nidaqmx.Task() as task2:
#        task2.do_channels.add_do_chan("cDAQ2Mod4/port0/line0:1", line_grouping=LineGrouping.CHAN_PER_LINE)
#        data2=task2.wite([True,False])
	actionlist=[]
	openreqlist=[]
	openenblist=[]
	closereqlist=[]
	for i in list:
		#for j in list1:	
			#print(i+j,bool(int(caget(i+j))))
		#print('\t')
	#print('\n')
		
		actionlist.append(bool(int(caget(i+"OPEN_ACT"))))
		openreqlist.append(bool(int(caget(i+"OPEN_REQ"))))
		openenblist.append(bool(int(caget(i+"OPEN_ENB"))))
		closereqlist.append(bool(int(caget(i+"CLOSE_REQ"))))
	#k=k+1
	#print("\033[F")
	print(''.join(str(actionlist)))
	print(''.join(str(openreqlist)))
	print(''.join(str(openenblist)))
	print(''.join(str(closereqlist)))
	#print(actionlist)
	time.sleep(1)
#    print('1 Channel 1 Sample Read Raw: ')
    

    
    
#    data = task.read_raw()

#    pp.pprint(data)
        #print("BL132:Iz",statistics.mean(data0)," ","BL132:Io",statistics.mean(data1),end='\r')
#    BL132_Io=statistics.mean(data1)
#    BL132_Iz=statistics.mean(data0)
#    BL132_Is=statistics.mean(data3)

#    print("{:8.3f}".format(BL132_Iz),"{:8.3f}".format(BL132_Io),"{:8.3f}".format(BL132_Is),end='\r')    
        #print("BL132:Id",statistics.mean(data2))
        #print("BL132:Is",statistics.mean(data3))
        #print("BL132:m1yaw_2_LVDT",statistics.mean(data4))
        #print("BL132:m2pit_2_LVDT",statistics.mean(data5))
        #print("AI6",statistics.mean(data6))
        #print("AI7",statistics.mean(data7))
    
#    caput("BL132:Iz",statistics.mean(data0))    
#    caput("BL132:Io",statistics.mean(data1))
#    caput("BL132:Id",statistics.mean(data2))
#    caput("BL132:Is",statistics.mean(data3))
#    caput("BL132:m1yaw_2_LVDT",statistics.mean(data4))
#    caput("BL132:m2pit_2_LVDT",statistics.mean(data5))