import os
import paramiko
import sys 
import time

#import pdb
#function definition
#def conn(host,port,username,password):
#host = sys.argv[1]
#username=sys.argv[2]
#password =sys.argv[3]
#pdb.set_trace()
def conn(hostname,username,keyfile):
    """ connection to server is established and the output is read from server."""
    rm = paramiko.SSHClient()
    rm.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    rm.connect(hostname=hostname,username=username,key_filename=key_filename)
    stdin, stdout, stderr = rm.exec_command("ls")
    val =stdout.read()
    #print val
    return val
if __name__ == "__main__":
    hostname=sys.argv[1]
    username=sys.argv[2]
    key_filename ="/opt/testkey.pem"
    try:
       a=conn(hostname,username,key_filename)
       print a
       print conn.__doc__
    except:
       print "server not reachable wait for few seconds"
       time.sleep(10)        
       

