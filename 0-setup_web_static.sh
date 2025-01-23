#!/usr/bin/env bash
# The script sets up the web servers for the deployment of web_static.

# Install Nginx if not installed
if ! dpkg -l | grep -q nginx; then
  sudo apt-get update
  sudo apt-get install -y nginx
fi

# Create given directories and folders if they don't exist
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared

# Create fake html file in the test release folder
echo "<html>
    <head>
    </head>
    <body>
        Holberton School
    </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Create a symbolic link if it doesnt exists or recreate it
if [ -L /data/web_static/current ]; then
    sudo rm /data/web_static/current
fi
sudo ln -s /data/web_static/releases/test /data/web_static/current

# Change ownership of /data/ to the ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration to serve /data/web_static/current to hbnb_static
sudo sed -i '/server {/a \\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

# Restart Nginx to apply changes
sudo systemctl restart nginx

# Exit successfully
exit 0