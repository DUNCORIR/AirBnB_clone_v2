#!/usr/bin/python3
"""
A  Fabric script that generates a .tgz archive from the
contents of the web_static folder
"""

from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.
    The archive is saved in the 'versions' folder.
    Returns:
        The path to the archive if successful, otherwise None.
    """
    # Ensure the 'versions' folder exists
    if not os.path.exists("versions"):
        os.makedirs("versions")

    # Generate the archive name with the current date and time
    current_time = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = f"versions/web_static_{current_time}.tgz"

    # Create the archive
    try:
        local(f"tar -cvzf {archive_name} web_static")
        return archive_name
    except Exception as e:  # Catch general exceptions and log the error
        print(f"An error occurred: {e}")
        return None


if __name__ == "__main__":
    result = do_pack()
    if result:
        print(f"Archive created: {result}")
    else:
        print("Failed to create archive.")
