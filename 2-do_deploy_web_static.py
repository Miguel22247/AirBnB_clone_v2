#!/usr/bin/python3
"""Script that does the deployment"""
import os
from fabric.api import *
from fabric.api import run, put


env.hosts = ['34.139.167.198', '34.138.129.5']


def do_deploy(archive_path):
    """Distributes an archive to your web servers"""

    if not os.path.exists(archive_path):
        return False
    else:
        try:
            put(archive_path, "/tmp/")
            filename = archive_path.split('/', 1)
            no_ext = filename[1].split('.', 1)
            archive = no_ext[0]
            run("mkdir -p /data/web_static/releases/" + archive + "/")
            run("tar -zxf /tmp/" + filename[1] +
                " -C /data/web_static/releases/" +
                archive + "/")
            run("rm /tmp/" + filename[1])
            run("mv /data/web_static/releases/" + archive +
                "/web_static/* /data/web_static/releases/" + archive + "/")
            run("rm -rf /data/web_static/releases/" + archive + "/web_static")
            run("rm -rf /data/web_static/current")
            run("ln -s /data/web_static/releases/" + archive +
                "/ /data/web_static/current")
            print("New version deployed!")
            return True
        except:
            return False
