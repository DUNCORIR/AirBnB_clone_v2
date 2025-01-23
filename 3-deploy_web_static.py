#!/usr/bin/python3
"""
Fabric script that creates and distributes an archive to web servers.
"""

from fabric.api import env, local, put, run
from datetime import datetime
import os

# Define the IP addresses of web servers
env.hosts = ['34.204.101.142', '100.25.12.114']  # Replace with your server IPs
env.user = 'ubuntu'  # Username for the servers
env.key_filename = '~/.ssh/id_rsa'  # Path to SSH private key


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.
    Returns:
        The path to the archive if successful, otherwise None.
    """
    # Ensure the 'versions' folder exists
    if not os.path.exists("versions"):
        os.makedirs("versions")

    # Generate the archive name with the current date and time
    current_time = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = os.path.join("versions", f"web_static_{current_time}.tgz")

    # Create the archive
    try:
        local(f"tar -cvzf {archive_name} web_static")
        return archive_name
    except Exception as e:
        print(f"An error occurred during archiving: {e}")
        return None


def do_deploy(archive_path):
    """
    Deploys an archive to the web servers.
    Args:
        archive_path (str): The path to the archive file.
    Returns:
        True if all operations are successful, otherwise False.
    """
    if not os.path.exists(archive_path):
        return False

    # Extract the archive name and its base name (without extension)
    archive_name = os.path.basename(archive_path)
    archive_base = os.path.splitext(archive_name)[0]
    release_path = f"/data/web_static/releases/{archive_base}"

    try:
        # Upload the archive to the /tmp/ directory
        put(archive_path, f"/tmp/{archive_name}")

        # Create the release directory
        run(f"mkdir -p {release_path}")

        # Uncompress the archive into the release directory
        run(f"tar -xzf /tmp/{archive_name} -C {release_path}")

        # Remove the uploaded archive from the server
        run(f"rm /tmp/{archive_name}")

        # Move the files to the correct location
        run(f"mv {release_path}/web_static/* {release_path}/")
        run(f"rm -rf {release_path}/web_static")

        # Delete the old symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link pointing to the new release
        run(f"ln -s {release_path} /data/web_static/current")
        run("sudo chown -R ubuntu:ubuntu /data/")
        return True
    except Exception as e:
        print(f"An error occurred during deployment: {e}")
        return False


def deploy():
    """
    Creates and distributes an archive to web servers.
    Returns:
        True if the deployment was successful, otherwise False.
    """
    # Call do_pack() to create an archive
    archive_path = do_pack()
    if not archive_path:
        return False

    # Deploy the archive to the web servers
    return do_deploy(archive_path)
