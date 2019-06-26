"""Script allow connect via SSH and RESTART OS services with followed is_active verification """
import time
import paramiko
import ssh_conf as conf_file

# Local variables
LOGIN = conf_file.USERNAME
PASSWORD = conf_file.PASSWORD
PORT = conf_file.PORT
TIMEOUT = conf_file.TIMEOUT

# ------------------------------------------------------------------------------------------


def ssh_command(client):
    """
    Get SSH connection, Get user input(service)
    """
    client.invoke_shell()
    stdin, stdout, stderr = client.exec_command('{command} {service} {action}'
                                                .format(command='sudo service',
                                                        service=service_name, action='restart'))

    print(stdout.read())

# ------------------------------------------------------------------------------------------


def is_service_running(client):
    client.invoke_shell()
    stdin, stdout, stderr = client.exec_command('{command} {service}'
                                                .format(command='sudo systemctl is-active',
                                                        service=service_name))
    print(stdout.read())


# ------------------------------------------------------------------------------------------


def ssh_connector():
    # Run over the servers IP's in a list
    with open('C:/Users/Totti10/PycharmProjects/otus-qa-course/'
              'less21/servers_list.txt', 'r') as file:
        for line in file:
            info = {}
            info['ip'] = line.split(' ')[0]
            info['hostname'] = line.split(' ')[1]
            info['location'] = line.split(' ')[2]
    try:
        print("Connecting to server.")
        # Create SSH client and set Auto policy to add host to ~/.ssh/known_hosts file
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # Connect to host
        client.connect(info['ip'], username=LOGIN, password=PASSWORD,
                       port=PORT, timeout=TIMEOUT, look_for_keys=False)

        # Get SSH Command
        ssh_command(client)
        # Verify service status
        is_service_running(client)

        time.sleep(1)
        client.close()

    except Exception as e:
        error_log = str(e)
        print(error_log + '\n')


# --------- START --------------------------------------------------------------------------


if __name__ == "__main__":
    service_name = input("Enter service name to restart: ")
    ssh_connector()
