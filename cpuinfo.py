import sys
import paramiko
import os
import argparse
import pdb


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

class SystemInfo:
    def __init__(self):
      pass

    def get_cpu(self, ssh_connection):
        cpu_info=[]
        stdin,stdout,stderr = ssh_connection.execute_command("lscpu")
        cpu_info.append(stdout.read())
        return cpu_info

if __name__ == "__main__":
    sys_info = SystemInfo()
    parser = argparse.ArgumentParser(description="validation for logging")
    parser.add_argument('--hostname',help='enter valid hostname for instance',required=True)
    parser.add_argument('--username',help='enter valid username for instance',required=True)
    #parser.add_argument('--password',help='enter the password for instance',required=False)
    parser.add_argument('--key_filename',help='specify the key_filename path',required=False)
    args = vars(parser.parse_args())
    #print args
    if not(args['username'] or args['hostname']):
         print "prime argument missing"
    #elif  not(args['password']):
     #    print"password missing"
    #elif not (args['--key_filename']):
     #    print"key_filename  missing"
    else:
         ssh_connection = Sshclient(hostname=args['hostname'], username=args['username'],key_filename=args['key_filename'])
         a2=sys_info.get_cpu(ssh_connection)
         print("cpu_info are : {0}".format(a2))
           
