
from paramiko import SSHClient 
import paramiko
import sys

#192.168.203. X
IP = '192.168.203.9'
USERNAME = 'noturno'
PASSWORD = 'noturno'
class SSH:
    def __init__(self):
        self.ssh = SSHClient()
        self.ssh.load_system_host_keys()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(hostname= IP, username=USERNAME, password=PASSWORD)
        
    def exec_cmd(self, comando):
        stdin,stdout,stderr = self.ssh.exec_command(comando)
        if stderr.channel.recv_exit_status() !=0:
            print(stderr.read())
        else:
            print(stdout.read())


if __name__ =='__main__':    
    ssh = SSH()
    ssh.exec_cmd("ls -l")

