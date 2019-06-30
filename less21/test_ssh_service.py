"""Script allow connect via SSH and RESTART OS services with followed is_active verification """
import time
import paramiko
import pytest
from less21.old import ssh_conf as conf_file


# Local variables
LOGIN = conf_file.USERNAME
PASSWORD = conf_file.PASSWORD
PORT = conf_file.PORT
TIMEOUT = conf_file.TIMEOUT

# ------------------------------------------------------------------------------------------


# def ssh_command(client):
#     """
#     Get SSH connection,
#     """
#     stdin, stdout, stderr = client.exec_command('{command} {service} {action}'
#                                                 .format(command='sudo service',
#                                                         service='apache2', action='restart'))
#
#     print(stdout.read())
#     print('Restart service')

# ------------------------------------------------------------------------------------------

# def is_service_running(client):
#
#     stdin, stdout, stderr = client.exec_command('{command} {service}'
#                                                 .format(command='sudo systemctl is-active',
#                                                         service='apache2'))
#     print(stdout.read())
#     result = str(stdout.read())
#     return result
#

# ------------------------------------------------------------------------------------------

@pytest.fixture(scope="module")
def ssh_connector():
    """ Connect to the servers restart services and check statuses"""
    # Run over the servers IP's in a list
    with open('servers_list.txt', 'r') as file:
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
        client.exec_command('sudo service restart')
        print('Restart service')

        # Verify service status
        _, stdout, stderr = client.exec_command('{command} {service}' .format
                                                (command='sudo systemctl is-active', service='apache2'))
        time.sleep(1)
        client.close()
        data = str(stdout.read())
        print(data)
        return data

    except Exception as e:
        error_log = str(e)
        print(error_log + '\n')


# ------------------------------------------------------------------------------------------


def test_is_service_active(ssh_connector):
    """ Verify service response"""
    result = ssh_connector
    assert 'active' in result
