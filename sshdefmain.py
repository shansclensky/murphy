import sys
import paramiko
import os
#import pdb
#function definition
#def conn(host,port,username,password):
#host = sys.argv[1]
#username=sys.argv[2]
#password =sys.argv[3]
#pdb.set_trace()
class sshclient:
    def __init__(self,hostname=10.16.86.156,port=22,password,key_filename):
    #def conn(hostname,port,username,password,key_filename):
    """ connection to server is established and the output is read from server."""
    #username password do ssh or keypassed means do ssh accodingly  as specified in the 
    self.ssh=paramiko.SSHClient()
    self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    self.ssh.connect(hostname=hostname,port=port , username=username, password=password,key_filename=key_filename)
    #stdin, stdout, stderr = rm.exec_command("")
    #stdout.read()
    
def get_cpuutilization(self):
    stdin,stdout,stderr =self.exec_command("top")
    cpu_info=stdout.read()
    return cpu_info

def get_memoryutilization(self):
    stdin,stdout,stderr = self.exec_commad("free -m")
    memory_info=stdout.read()
    return memory_info

def get_portstatistics(self):
    stdin.stdout,stderr = self.exec_command("netstat -i")
    port_info=stdout.read()
    return port_info
if __name__ == "__main__":
    hostname=sys.argv[1]
    port=int(sys.argv[2])
    username=sys.argv[3]
    password =sys.argv[4]
    key_filename="/opt/testkey.pem"
    s1 = sshclient(hostname,port,username,password,key_filename)
    if argv[4]==0:
       a0= s1.get_cpuutilizaton()
       a1= s1.get_memoryutilization()
       a2=s1.get_portstatistics()
       print a0,a1,a2
       #print conn.__doc__
    
    else:
       b =comm(hostname,port,username,keyfile_name)
       b0=s1.get_cpuutilizaton()
       b1=s2.get_memoryutilization()
       b2=s3.get_portstatistics()
       print b0,b1,b2 
 



