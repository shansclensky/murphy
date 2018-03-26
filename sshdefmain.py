import sys
import paramiko
#import pdb
#function definition
#def conn(host,port,username,password):
#host = sys.argv[1]
#username=sys.argv[2]
#password =sys.argv[3]
#pdb.set_trace()
def conn(hostname,port,username,password):
    """ connection to server is established and the output is read from server."""
    rm = paramiko.SSHClient()
    rm.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    rm.connect(hostname=hostname,port=port , username=username, password=password)
    stdin, stdout, stderr = rm.exec_command("ls")
    val =stdout.read()
    #print val 
    return val
if __name__ == "__main__":
    hostname=sys.argv[1]
    port=int(sys.argv[2])
    username=sys.argv[3]
    password =sys.argv[4]
    a=conn(hostname,port,username,password)
    print a
    print conn.__doc__

 



