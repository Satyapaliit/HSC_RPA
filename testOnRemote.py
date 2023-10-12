import paramiko

# Define SSH connection details
host = "your_remote_host"
port = 22  # SSH port
username = "your_username"
password = "your_password"  # Consider using SSH keys for more security

# Create an SSH client
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    # Connect to the remote machine
    ssh_client.connect(host, port, username, password)

    # Execute a command remotely (replace with your test command)
    command = "your_test_command"
    stdin, stdout, stderr = ssh_client.exec_command(command)

    # Print the output of the remote command
    print(stdout.read().decode())

finally:
    # Close the SSH connection
    ssh_client.close()
