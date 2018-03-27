import sys
import paramiko
#import pdb
#function definition
#def conn(host,port,username,password):
#host = sys.argv[1]
#username=sys.argv[2]
#password =sys.argv[3]
#pdb.set_trace()
def conn(hostname,port,username,password,key_filename):
    """ connection to server is established and the output is read from server."""
    #username password do ssh or keypassed means do ssh accodingly  as specified in the 
    clientssh = paramiko.SSHClient()
    clientssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    res = clientssh.connect(hostname=hostname,port=port , username=username, password=password,key_filename=key_filename)
    #stdin, stdout, stderr = rm.exec_command("")
    #stdout.read()
    return res

def get_cpuutilization(res):
    stdin,stdout,stderr = clientssh.exec_command("top")
    cpu_info=stdout.read()
    return cpu_info

def get_memoryutilization(res):
    stdin,stdout,stderr = clientssh.exec_commad("free -m")
    memory_info=stdout.read()
    return memory_info

def get_portstatistics(res):
    stdin.stdout,stderr = clientssh.exec_command("netstat -i")
    port_info=stdout.read()
    return port_info
if __name__ == "__main__":
    hostname=sys.argv[1]
    port=int(sys.argv[2])
    username=sys.argv[3]
    password =sys.argv[4]
    key_filename="/opt/testkey.pem"
    if argv[4]==0:
       a=conn(hostname,port,username,password)
       a0=get_cpuutilizaton(res)
       a1=get_memoryutilization(res)
       a2=get_portstatistics(res)
       print a0,a1,a2
       #print conn.__doc__
    else:
        try:
           
        b =comm(hostnamem,port,username,keyfile_name)
        b0= get_cpuutilizaton(res)
        b1=get_memoryutilization(res)
        b2=get_portstatistics(res)
       print b0,b1,b2 
 



