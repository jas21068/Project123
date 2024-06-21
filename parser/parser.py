import sys
import os
import paramiko
import time
import argparse

#

def main():
    parser = argparse.ArgumentParser(description='A script to connect to a server and execute commands')

    # Add arguments
    parser.add_argument('-s', '--Source', type=str, required=True, help='The sorce commands')
    parser.add_argument('-d', '--Dest', type=str, required=True, help='The output file')

    # Parse the arguments
    args = parser.parse_args()

    # Use the arguments
    print(f'Input file: {args.Source}')
    print(f'output file: {args.Dest}')
    try:
        with open(f'{args.Source}') as text_file:
            a = text_file.readlines()
    except:
        print("wrong src file try again from scratch")
        sys.exit(1)

#    a = ['get router info routing-table all\n', 'diag hardware sysinfo memory\n']
 #   b = ['show route | no-more | grep B\n', 'show configuration| no-more\n']

    ssh_client = paramiko.SSHClient()
    print(type(ssh_client))

    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ip = input('What is the ip\n')
    port = input('What is the port\n')
    user = input('What is the username\n')
    pwd = input('What is the password\n')

    router1 = {'hostname': ip, 'port': port, 'username': user, 'password': pwd}
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
       # print(output)
        # print(type(output))
        output1 = output.decode('utf-8')  # decoding from bytes to string
        print(output1)
        with open(f"{args.Dest}", "w") as text_file4:
       	    text_file4.write(output1)
        # closing the connection if it's active
        if ssh_client.get_transport().is_active() == True:
            print('Closing connection')
            ssh_client.close()

    router1_connect()







main()













