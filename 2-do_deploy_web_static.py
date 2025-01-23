#!/usr/bin/python3
"""
Fabric script to deploy an archive on server using do__deploy function.
"""
from fabric.api import env, put, run
import os

# Define the IP addresses of web servers
env.hosts = ['34.204.101.142', '100.25.12.114']  # Replace with your server IPs
env.user = 'ubuntu'  # Username for your servers
env.key_filename = '~/.ssh/id_rsa'  # Path to SSH private key


def do_deploy(archive_path):
    """
    Deploys an archive to the web servers.
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

        # Uncompress the archive to the release directory
        run(f"tar -xzf /tmp/{archive_name} -C {release_path}")

        # Remove the uploaded archive from the server
        run(f"rm /tmp/{archive_name}")

        # Move the files to the correct location
        run(f"mv {release_path}/web_static/* {release_path}/")
        run(f"rm -rf {release_path}/web_static")

        # Delete the old symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run(f"ln -s {release_path} /data/web_static/current")

        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
