import os
import paramiko
import sys 
import sys
import paramiko
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
    rm.connect(hostname=hostname,username=username,keyfile=keyfile)
    stdin, stdout, stderr = rm.exec_command("ls")
    val =stdout.read()
    #print val
    return val
if __name__ == "__main__":
    hostname=sys.argv[1]
    username=sys.argv[3]
    keyfile =/opt/testkey.pem
    a=conn(hostname,username,keyfile)
    print a
    print conn.__doc__

