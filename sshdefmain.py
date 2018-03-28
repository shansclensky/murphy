import sys
import paramiko
import os
import argparse
#import pdb
#function definition
#def conn(host,port,username,password):
#host = sys.argv[1]
#username=sys.argv[2]
#password =sys.argv[3]
#pdb.set_trace()

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
 
    #stdin, stdout, stderr = rm.exec_command("")
    #stdout.read()
    
    def get_cpuutilization(self):
        stdin,stdout,stderr =self.ssh.exec_command("top")
        cpu_info=stdout.read()
        return cpu_info
    
    def get_memoryutilization(self):
        stdin,stdout,stderr = self.ssh.exec_commad("free -m")
        memory_info=stdout.read()
        return memory_info
    
    def get_portstatistics(self):
        stdin.stdout,stderr = self.ssh.exec_command("netstat -i")
        port_info=stdout.read()
        return port_info
if __name__ == "__main__":
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
         s1 = Sshclient(hostname=args['hostname'], username=args['username'],password=args['password'])
         a0= s1.get_cpuutilizaton()
         a1= s1.get_memoryutilization()
         a2=s1.get_portstatistics()
         print a0,a1,a2
   #print conn.__doc__
    
 
 



