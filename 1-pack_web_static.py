#!/usr/bin/python3
from fabric.api import local
from datetime import datetime


def do_pack():
    time = datetime.now().strftime("%Y%m%d%H%M%S")
    file_backup = "versions/web_static_{:s}.tgz".format(time)
    try:
        local("mkdir -p ./versions")
        local("tar -cvzf {:s} web_static".format(file_backup))
    except:
        return None
