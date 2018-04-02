from time import sleep
import sys
import paramiko
import os
import argparse
import re
import pdb
import re
#function definition
#def conn(host,port,username,password):
#host = sys.argv[1]
#username=sys.argv[2]
#password =sys.argv[3]


class Sshclient:
    def __init__(self,hostname=None,port=22,username=None,password=None,key_filename=None):
        #def conn(hostname,port,username,password,key_filename):
        """ connection to server is established and the output is read from server."""
        #username password do ssh or keypassed means do ssh accodingly  as specified in the 
        if password==None:
          self.ssh=paramiko.SSHClient()
          self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
          self.ssh.connect(hostname=hostname,port=port, username=username,key_filename=key_filename)
        else:
          self.ssh=paramiko.SSHClient()
          self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
          self.ssh.connect(hostname=hostname,port=port, username=username,password=password)

    def execute_command(self, command):
        stdin,stdout,stderr = self.ssh.exec_command(command)
        return stdin,stdout,stderr
     
    def interative_shell(self):
        remote_conn = self.ssh.invoke_shell()
        return remote_conn
     
    #stdin, stdout, stderr = rm.execute_command("")
    #stdout.read()

class SystemInfo:
    def __init__(self):
      pass
 
    def get_cpuutilization(self, ssh_connection):
        #stdin,stdout,stderr =self.ssh.execute_command("/proc/stat")
        global worktime,idletime,line,dif
	stdin,stdout,stderr = ssh_connection.execute_command("cat /proc/stat")
        #pdb.set_trace()
        value =stdout.readlines()
    	#$line = re.sub('cpu0',"",line2)
        #while not "cpu " in line:
         #    line=f.readline()"""
	print value 
        line=value[0]
        print line
        d=line.split(" ")
        print d	
        worktime= int(d[2])+int(d[3])+int(d[4])+int(d[6])+int(d[7])+int(d[8])+int(d[5])
        print worktime
        idletime=int(d[5])+int(d[6])
	print idletime
        dif =worktime - idletime
        print dif 
        rate=float(dif)/(worktime)
        print rate
        cpu_info=float(rate*100)
        print cpu_info
        #dworktime=(worktime-last_worktime)
	#didletime=(idletime-last_idletime)
	#pdb.set_trace()
        #last_worktime=worktime
	#last_idletime=idletime
 	if(worktime==0):
           return 0
	else:
           return cpu_info
        #cpu_info=stdout.read()
        #return cpu_info
    
    def get_memoryutilization(self, ssh_connection):
        stdin,stdout,stderr = ssh_connection.execute_command("free | grep Mem | awk '{print $2}'")
        m1=stdout.read()
        #print m1
        stdin,stdout,stderr = ssh_connection.execute_command("free | grep Mem | awk '{print $3}'")
        m2=stdout.read()
        #print m2  
        stdin,stdout,stderr = ssh_connection.execute_command("free | grep Mem | awk '{print $4}'")
        m3=stdout.read()
        memused= float(m2)/float(m1)
        percent_memused = memused*100.0
        #print percent_memused        
        memfree= float(m3)/float(m1)
        percent_memfree = memfree*100.0
        mem_info ={"percent_memfree":percent_memfree,"percent_memused":percent_memused}
        return mem_info
        #return percent_memused,percent_memfree
        #def get_percent_memused(self,ssh_connection.execute_command("free |grep ")
        #rint percent_memfree
        #v1 = mem.split(" ")
        #print v1 
        #memory_info =float(v1[22])/float(v1[32])
        #info = 
        #print info
        #return m1 
        #return memory_info
    
    def get_portstatistics(self, ssh_connection):
        #pdb.set_trace()
        remote_conn = ssh_connection.interative_shell()
        remote_conn.send('ip link show \n')
        sleep(1)
        output1= remote_conn.recv(7000)
        print output1
        interf= re.findall(r": (.*?):",output1)
        print interf
        interface={"interface name":interf}
        print interface
        remote_conn.send('ifconfig \n')
        sleep(5)
        output = remote_conn.recv(5000)
        print output
        #for i in interface:
        value = re.search(r"eth0\s+(.*\n\s+)*?RX packets:(\d+)(.*\n\s+)*?TX packets:(\d+)",output)
        #print re.search(r"{}\s+(.*\n\s+)*?RX packets:(\d+)(.*\n\s+)*?TX packets:(\d+)",output).format(eth0)
        #print value
        print value.group(2)       
        print value.group(4) 
        port_info_inp = {"interfacename":interf[1],"RX PACKETS":value.group(2),"TX PACKETS":value.group(4)}
        #print port_info_inp
             
        #print "1enter the name of interface to know its port statistics"
               
        #print output1
        #port = re.findall(r"(?<=Metric)[^-.]*",output)
	#print(port)
        	
        return port_info_inp
if __name__ == "__main__":
    sys_info = SystemInfo()
    parser = argparse.ArgumentParser(description="validation for logging")
    parser.add_argument('--hostname',help='enter valid hostname',required=True)
    parser.add_argument('--username',help='enter valid username',required=True)
    parser.add_argument('--password',help='enter the password',required=False)
    #parser.add_argument('--key_filename',help='specify the key_filename path',required=False)
    args = vars(parser.parse_args())
    print args
    if not(args['username'] or args['hostname']):
         print "prime argument missing"
    elif  not(args['password']): 
         print"password missing "
    #elif not args['--key_filename']):
     #    print"key_filename missing"
    else:
         ssh_connection = Sshclient(hostname=args['hostname'], username=args['username'],password=args['password'])
         a2=sys_info.get_portstatistics(ssh_connection)
         a0= sys_info.get_cpuutilization(ssh_connection)
         print("cpu_util:{0}%".format(a0))
         #print("percent_memfree :{0}%".format(a0))
         a1= sys_info.get_memoryutilization(ssh_connection)
         print("mem_util : {0}%".format(a1))
         print("port_stat : {0}".format(a2))
   #print conn.__doc__
    
 
 



