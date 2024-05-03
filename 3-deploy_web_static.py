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
    try:
        local("tar -cvzf versions/{} web_static"
              .format(archive_name))
        print("web_static packed: {} -> {}Bytes"
              .format(arcpath, os.path.getsize(arcpath)))
        return arcpath
    except Exception:
        raise
    


@runs_once
def do_alx(archive_path):
    try:
        archive_fname = os.path.basename(archive_path)
        archive_name = archive_fname.split(".")[0]
        folder = "/data/web_static/releases"
        local("cp {} /tmp/{}".format(archive_path, archive_fname))
        local("mkdir -p {}/{}".format(folder, archive_name))
        local("mkdir -p /data/web_static/shared/")
        local("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
              .format(archive_fname, archive_name))
        local("rm /tmp/{}".format(archive_fname))
        local("mv {0}/{1}/web_static/* {0}/{1}/".format(folder, archive_name))
        local("rm -rf {}/{}/web_static".format(folder, archive_name))
        local("rm -rf /data/web_static/current")
        local("ln -s /data/web_static/releases/{}/ /data/web_static/current"
              .format(archive_name))
        return
    except Exception:
        raise


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
        sudo("chown -R ubuntu:ubuntu /data")
        run("mkdir -p /data/web_static/shared/")
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
            .format(archive_fname, archive_name))
        run("rm /tmp/{}".format(archive_fname))
        run("mv {0}/{1}/web_static/* {0}/{1}/".format(folder, archive_name))
        run("rm -rf {}/{}/web_static".format(folder, archive_name))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(archive_name))
        print("New version deployed!")
        return True
    except Exception:
        raise


@task
def deploy():
    """ pack and deploy"""
    path_arc = do_pack()
    if path_arc is None:
        return False
    do_alx(path_arc)
    return do_deploy(path_arc)
