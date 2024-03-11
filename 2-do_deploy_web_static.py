#!/usr/bin/env python3
"""Fabric script (based on the file 1-pack_web_static.py) that distributes
an archive to your web servers, using the function do_deploy"""

from fabric.api import env, put, run, sudo
import os

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
