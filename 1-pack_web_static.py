#!/usr/bin/python3
""" Script that compress files using .tgz"""
from fabric.api import run, local
from datetime import datetime


def do_pack():
    """function that generates .tgz file"""

    format_d = "%Y%m%d%H%M%S"
    try:
        local("mkdir -p versions")
        date = datetime.now()
        filename = "versions/web_static_" + date.strftime("%Y%m%d%H%M%S") + ".tgz"
        local("tar -cvzf " + filename + " web_static")
        return filename
    except:
        return None
