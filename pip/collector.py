
import os
import paramiko
import time

with open("fgt_commands") as text_file:
    a = text_file.readlines()
    
with open("junos_commands") as text_file2:
    b = text_file2.readlines()

print(a)
print(b)    
#a = ['get router info routing-table all\n', 'diag hardware sysinfo memory\n']
#b = ['show route | no-more | grep B\n', 'show configuration| no-more\n']

ssh_client = paramiko.SSHClient()
print(type(ssh_client))

ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())





router1 = {'hostname': '172.16.1.1', 'port': '22', 'username': 'admin', 'password': 'admin'}
router2 = {'hostname': '172.16.1.101', 'port': '22', 'username': 'admin', 'password': 'Jaskirat2512+'}

def router1_connect():
    print(f'Connecting to {router1["hostname"]}')
    ssh_client.connect(**router1, look_for_keys=False, allow_agent=False)

    # creating a shell object
    shell = ssh_client.invoke_shell()
    time.sleep(4)
    # sending commads to the remote device to execute them
    # each command ends  in \n (new line, the enter key)
    for i in a:
        print(i)
        shell.send(i)
    #
    # shell.send('get system status\n')
    # shell.send('get system performance status\n')
    # shell.send('get router info routing-table all\n')
    time.sleep(10)  # waiting for the remove device to finish executing the commands (mandatory)

    # reading from the shell's output buffer
    output = shell.recv(10000000)
#    print(output)
    # print(type(output))
    output1 = output.decode('utf-8')  # decoding from bytes to string
 #   print(output1)
    with open("FGT_OUTPUT", "w") as text_file3:
       text_file3.write(output1)
    # closing the connection if it's active
    if ssh_client.get_transport().is_active() == True:
        print('Closing connection')
        ssh_client.close()

def router2_connect():
    print(f'Connecting to {router2["hostname"]}')
    ssh_client.connect(**router2, look_for_keys=False, allow_agent=False)

    shell = ssh_client.invoke_shell()
    time.sleep(4)

    for i in b:
        print(i)
        shell.send(i)

    time.sleep(10)  # waiting for the remove device to finish executing the commands (mandatory)

    output = shell.recv(10000000)
 #   print(output)
    output1 = output.decode('utf-8')  # decoding from bytes to string

 
    with open("JUNOS_OUTPUT", "w") as text_file4:
       text_file4.write(output1)
    # closing the connection if it's active
    if ssh_client.get_transport().is_active() == True:
        print('Closing connection')
        ssh_client.close()



router1_connect()
router2_connect()



















