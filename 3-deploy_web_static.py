#!/usr/bin/python3
""" deploy web_static as archive """
from fabric.api import run, put, task, env, local, runs_once, sudo
import datetime
import os


env.hosts = ["100.25.41.53", "52.3.253.7"]


@runs_once
def do_pack():
    """ pack as tgz archive """
    current_time = datetime.datetime.now()
    formatted = current_time.strftime("%Y%m%d%H%M%S")
    archive_name = "web_static_{}.tgz".format(formatted)
    arcpath = "versions/" + archive_name
    local("mkdir -p versions")
    print("Packing web_static to {}".format(arcpath))
    if local("tar -cvzf versions/{} web_static"
             .format(archive_name)).succeeded:
        print("web_static packed: {} -> {}Bytes"
              .format(arcpath, os.path.getsize(arcpath)))
        return arcpath
    return None


@task
def do_deploy(archive_path):
    """ deploy tgz archive """
    try:
        if not os.path.exists(archive_path):
            return False
        archive_fname = os.path.basename(archive_path)
        archive_name = archive_fname.split(".")[0]
        folder = "/data/web_static/releases"
        put(archive_path, "/tmp/")
        sudo("mkdir -p {}/{}".format(folder, archive_name))
        sudo("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
             .format(archive_fname, archive_name))
        sudo("rm /tmp/{}".format(archive_fname))
        sudo("mv {0}/{1}/web_static/* {0}/{1}/".format(folder, archive_name))
        sudo("rm -rf {}/{}/web_static".format(folder, archive_name))
        sudo("rm -rf /data/web_static/current")
        sudo("chmod +777 -R /data")
        sudo("ln -s /data/web_static/releases/{}/ /data/web_static/current"
             .format(archive_name))
        print("New version deployed!")
        return True
    except Exception:
        return False


@task
def deploy():
    """ pack and deploy"""
    path_arc = do_pack()
    if path_arc is None:
        return False
    return do_deploy(path_arc)
