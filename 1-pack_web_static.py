#!/usr/bin/python3
""" Script that compress files using .tgz"""
from fabric.api import run, local
from datetime import datetime


def do_pack():
    """Generates a .tgz archive"""
    
    format_d = "%Y%m%d%H%M%S"
    dir_path = "versions/web_static_"
    try:
        local("mkdir -p versions")
        date = datetime.now()
        filename = dir_path + date.strftime(format_d) + ".tgz"
        local("tar -cvzf " + filename + " web_static")
        return filename
    except:
        return None
