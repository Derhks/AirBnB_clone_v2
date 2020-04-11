#!/usr/bin/python3
from fabric.api import *
from datetime import datetime
import os
from sys import argv

env.hosts = ['35.231.33.237', '35.185.107.146']
env.user = argv[7]
env.password = argv[5]


def do_pack():
    """This method create a backup for the directory web_static"""
    time = datetime.now().strftime("%Y%m%d%H%M%S")
    file_backup = "versions/web_static_{:s}.tgz".format(time)
    try:
        local("mkdir -p ./versions")
        local("tar -cvzf {:s} web_static".format(file_backup))
    except:
        return None


def do_deploy(archive_path):
    """This method deploy the new file of the web_static"""
    if os.path.isfile(archive_path):
        try:
            remote_path = "/tmp/{:s}".format(archive_path[9:])
            path = "web_static/releases"
            put(archive_path, remote_path)
            run("mkdir -p /data/web_static/releases/{:s}".
                format(archive_path[9:-4]))
            run("tar -xzf /tmp/{:s} -C /data/web_static/releases/{:s}".
                format(archive_path[9:], archive_path[9:-4]))
            run("rm /tmp/{:s}".format(archive_path[9:]))
            run("mv /data/{:s}/{:s}/web_static/* /data/{:s}/{:s}"
                .format(path, archive_path[9:-4], path, archive_path[9:-4]))
            run("rm -rf /data/web_static/releases/{:s}/web_static".
                format(archive_path[9:-4]))
            run("rm -rf /data/web_static/current")
            run("ln -s /data/{:s}/{:s}/ /data/web_static/current".
                format(path, archive_path[9:-4]))
            return True
        except:
            return False
    else:
        return False
