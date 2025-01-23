#!/usr/bin/python3
"""
Fabric script that deletes out-of-date archives from local and remote servers.
"""

from fabric.api import env, local, run, sudo
import os

# Define the IP addresses of web servers
env.hosts = ['34.204.101.142', '100.25.12.114']  # Replace with your server IPs
env.user = 'ubuntu'  # Username for servers
env.key_filename = '~/.ssh/id_rsa'  # Path to SSH private key


def do_clean(number=0):
    """
    Deletes out-of-date archives.

    Args:
        number (int): The number of archives to keep. If 0 or 1, only the most
                      recent archive is kept. If 2, the two most recent
                      archives are kept, etc.
    """
    number = int(number)
    if number <= 0:
        number = 1

    # Delete out-of-date archives locally
    archives = sorted(os.listdir("versions"))
    archives_to_delete = archives[:-number]

    for archive in archives_to_delete:
        local(f"rm -rf versions/{archive}")

    # Delete out-of-date archives on remote servers
    releases_path = "/data/web_static/releases"
    try:
        # List all directories in the releases folder on the remote servers
        archives_remote = run(f"ls -1t {releases_path}").split()
        archives_to_delete_remote = archives_remote[number:]

        for archive in archives_to_delete_remote:
            run(f"rm -rf {releases_path}/{archive}")

    except Exception as e:
        print(f"An error occurred: {e}")
