from time import sleep
import sys
import paramiko
import os
import argparse
import re
import pdb
import math


class Sshclient:
    def __init__(self,hostname=None,port=22,username=None,password=None,key_filename=None):
        """ Connection to server is established and the output is read from server 
        Args:
            param hostname (str) : It is a host IP.ex:10.16.67.78
            param port (int) : Default SSH port
            param username (str) : SSH user
            param password (str) : SSH password
            param key_filename (str) : It is SSH key_pair file of format .pem.ex: testkey.pem
        """
        self.ssh=paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        if(password==None):
            self.ssh.connect(hostname=hostname,port=port,username=username,key_filename=key_filename)
        else:
            self.ssh.connect(hostname=hostname,port=port,username=username,password=password)
               
  
    def execute_command(self, command):
        stdin,stdout,stderr = self.ssh.exec_command(command)
        return stdin,stdout,stderr
     
    def interative_shell(self):
        remote_conn = self.ssh.invoke_shell()
        return remote_conn
     

def wait_for_device_avaialbility(hostname=None,port=22,username=None,key_filename=None):
    #wait some time
    sleep(10)
    ssh_connection=None
    available=False
    try:
        ssh_connection=Sshclient(hostname=hostname,port=22,username=username,key_filename=key_filename)
        available=True
        print("host '{0}'reachable".format(hostname))
        print("calculating characterstics from the instance")
    except:
        print("host '{0}' not reachable".format(hostname))
    return available,ssh_connection

   
 
class SystemInfo:
    def __init__(self):
      pass
 
    def get_cpuutilization(self, ssh_connection):
	cpu_info={}
        stdin,stdout,stderr = ssh_connection.execute_command("cat /proc/stat")
        value =stdout.readlines()
        line=value[0]
        d=line.split(" ")
        #worktime=nice+system+idle+iowait+iq+softiq+steal
        worktime= int(d[2])+int(d[3])+int(d[4])+int(d[6])+int(d[7])+int(d[8])+int(d[5])
        #idletime=idle+iowait
        idletime=int(d[5])+int(d[6])
        dif =worktime - idletime
        rate=float(dif)/(worktime)
        info_=float(rate*100)
        cpu_info=round(info_)
 	if(worktime==0):
           return 0
	else:
           return cpu_info
        
    
    def get_memoryutilization(self, ssh_connection):
        mem_info={}
        m1=[2,3,4]
        m2=[]
        for i in m1:
           stdin,stdout,stderr = ssh_connection.execute_command("free | grep Mem | awk '{print $%d}'"%(i))
           m2.append(stdout.read())
        mem={"total_mem":m2[0],"mem_used":m2[1],"mem_free":m2[2]}
        memused= float(m2[1])/float(m2[0])
        memused_ = memused*100.0
        percent_memused = round(memused_)
        memfree= float(m2[2])/float(m2[0])
        memfree_ = memfree*100.0
        percent_memfree =round(memfree_)
        return percent_memused,percent_memfree
    
    def get_portstatistics(self, ssh_connection):
        #pdb.set_trace()
        port_info ={}
        remote_conn = ssh_connection.interative_shell()
        remote_conn.send('ip link show \n')
        sleep(1)
        output1= remote_conn.recv(7000)
        interf= re.findall(r": (.*?):",output1)
        interface={"interface name":interf}
        remote_conn.send('ifconfig \n')
        sleep(5)
        output = remote_conn.recv(5000)
        for i in interf:
            value = "{0}\s+(.*\n\s+)*?RX packets:(\d+)(.*\n\s+)*?TX packets:(\d+)".format(i)
            value2 = re.search(value,output)
            port_info[i] = {"RX PACKETS":"{0} bytes".format(value2.group(2)),"TX PACKETS":"{0} bytes".format(value2.group(4))}
        return port_info
if __name__ == "__main__":
    sys_info = SystemInfo()
    parser = argparse.ArgumentParser(description="validation for logging")
    parser.add_argument('--hostname',help='enter valid hostname for instance',required=True)
    parser.add_argument('--username',help='enter valid username for instance',required=True)
    parser.add_argument('--key_filename',help='specify the key_filename path',required=False)
    args = vars(parser.parse_args())
    if not(args['username'] or args['hostname']):
         print "prime argument missing"
    else:
         ssh_connection = Sshclient(hostname=args['hostname'], username=args['username'],key_filename=args['key_filename'])
         a2=sys_info.get_portstatistics(ssh_connection)
         a0= sys_info.get_cpuutilization(ssh_connection)
         print("PERCENTAGE CPU_UTILIZED:{0}%".format(a0))
         #print("percent_memfree :{0}%".format(a0))
         a1= sys_info.get_memoryutilization(ssh_connection)
         print("PERCENTAGE MEM_FREE :{0}% ,PERCENTAGE MEM_AVAILABLE:{1}%".format(a1[0],a1[1]))
         #print("percent_memfree :{0}".format(a1))
         #print("mem_util : {0}".format(a1))
         print("PORT_STATISTICS :{0}".format(a2))
         #print("PORT_STATISTICS :'RX PACKETS':{0},'TX PACKETS':{1}".format(a2[0],a2[1]))
         
