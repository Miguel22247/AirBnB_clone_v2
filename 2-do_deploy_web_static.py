#!/usr/bin/python3
"""Script that does the deployment"""
from fabric.operations import local, run, put
from datetime import datetime
import os
import re
from fabric.api import env


env.hosts = ['34.139.167.198', '34.138.129.5']

def do_pack():
    """function to compress files """
    local("mkdir -p versions")
    return_command = local("tar -cvzf versions/web_static_{}.tgz web_static"
                   .format(datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")),
                   capture=True)
    if return_command.failed:
        return None
    return return_command

def do_deploy():
    """function to make the deployment"""
    if not os.path.exists(archived_path):
        return False
    rex = r'^versions/(\S+).tgz'
    match = re.search(rex, archive_path)
    filename = match.group(1)
    response = put(archive_path, "/tmp/{}.tgz".format(filename))
    if response.failed:
        return False
    response = run("mkdir -p /data/web_static/releases/{}/".format(filename))
    if response.failed:
        return False
    response = run("tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/"
              .format(filename, filename))
    if response.failed:
        return False
    response = run("rm /tmp/{}.tgz".format(filename))
    if response.failed:
        return False
    response = run("mv /data/web_static/releases/{}"
              "/web_static/* /data/web_static/releases/{}/"
              .format(filename, filename))
    if response.failed:
        return False
    response = run("rm -rf /data/web_static/releases/{}/web_static"
              .format(filename))
    if response.failed:
        return False
    response = run("rm -rf /data/web_static/current")
    if response.failed:
        return False
    response = run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
              .format(filename))
    if response.failed:
        return False
    print('New version deployed!')
    return True