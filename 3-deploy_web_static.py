#!/usr/bin/python3
"""Fabric script (based on the file 2-do_deploy_web_static.py)
that creates and distributes an archive to your web servers,
using the function deploy"""

import os
from fabric.api import env, put, run, sudo
from datetime import datetime
from fabric.api import local
import os


def do_pack():
    """generates a .tgz archive"""
    local("mkdir -p versions")
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    file = "web_static_{}.tgz".format(timestamp)
    t_file = local("tar -czvf versions/{} web_static".format(file))

    if t_file.failed:
        return None
    return file


env.hosts = ['35.174.200.196']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """distributes an archive to your web servers"""
    if not os.path.exists(archive_path):
        return False
    try:
        put(archive_path, '/tmp/')

        filename = os.path.basename(archive_path)
        folder_name = filename.split('.')[0]
        release_path = '/data/web_static/releases/{}'.format(folder_name)

        run('sudo mkdir -p {}'.format(release_path))
        run('tar -xzf /tmp/{} -C {}'.format(filename, release_path))

        run("sudo rm /tmp/{}".format(filename))

        current_link = '/data/web_static/current'
        run("sudo rm -f {}".format(current_link))

        run("ln -s {} {}".format(release_path, current_link))

        print("Deployment successful")
        return True
    except Exception as err:
        print("Deployment failed")
        return False


def deploy():
    """creates and distributes an archive to your web servers"""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
