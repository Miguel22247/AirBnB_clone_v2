#!/usr/bin/python3
""" Script that compress files using .tgz"""
from fabric.api import run, local
from datetime import datetime


def do_pack():
    
    format_d = "%Y%m%d%H%M%S"
    cmd = "mkdir -p versions"
    """Generates a .tgz archive"""
    try:
        local(cmd)
        date = datetime.now()
        filename = "versions/web_static_" + date.strftime(format_d) + ".tgz"
        local("tar -cvzf " + filename + " web_static")
        return filename
    except:
        return None
