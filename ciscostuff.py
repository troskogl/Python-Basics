#
#                                                                        
# Title: ciscostuff.py                                                 
# Author: Trond Skogland (trond.skogland@atea.no)                        
#                                                                        
# Description:                                                             
#         Diverse testing mot cisco router. Bruker paramiko library                                                               
#
import paramiko
import os
import sys

ssh = paramiko.SSHClient()
# Since we are not using host file.
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect('10.10.10.1',username='testuser', password='testuser')

channel = ssh.invoke_shell()
channel_data = str()
host = str()
srcfile = str()

clear = lambda: os.system('cls')

# channel.send()
# channel.recv(9999)
# channel.recv_ready()

while True:
	if channel.recv_ready():
		channel_data += channel.recv(9999)
		clear()
		print ('##### Device Output #####')
		print (channel_data)
		print ('########################')
	else:
	
	if channel_data.endswith('SKOGLAND-RT-819#'):
		channel.send('copy tftp: flash: \n')
	elif channel_data.endswith('remote host[]? '):
		host = raw_input('\n\n\tEnter the TFTP Host IP: ')
		channel.send(host)
		channel.send('\n')
	elif channel_data.endswith('Source filename []? '):
		srcfile = raw_input('\n\n\tEnter the Source File: ')
		channel.send(srcfile)
		channel.send('\n')
	elif channel_data.endswith(' Destination filename[{}]? '.format(srcfile)):
		channel.send('\n')
	elif '(Timed out)' in channel_data:
		print ('\nERROR: Connection to TFTP Server {} timed out'.format(host))
		channel_data = ''
		channel.send('\n')

# stdin, stdout, stderr = ssh.exec_command('show ip interface brief')


# output = stdout.readlines()

# # print (type (output))

# print ('\n'.join(output))

# ssh.connect('10.10.10.1',username='testuser', password='testuser')
# stdin, stdout, stderr = ssh.exec_command('copy tftp: flash:')

# stdin.write('10.10.10.1')
# stdin.write('\n')

# print(stdin)

# stdin.flush()

# stdin.write('vlan.dat')
# stdin.write('\n')
# stdin.flush()

# stdin.write('vlan.bak')
# stdin.write('\n')
# stdin.flush()

# output = stdout.readlines()
# print ('\n'.join(output))
# ssh.close()

#print (innput)