#!/usr/bin/python3
""" deploy web_static as archive """
from fabric.api import run, put, task, env, local
import os


env.hosts = ['web-01.bmworks.tech', 'web-02.bmworks.tech']


@task
def do_deploy(archive_path):
    """ deploy tgz archive """
    if not os.path.exists(archive_path):
        return False
    try:
        put(archive_path, '/tmp/')
        archive_fname = os.path.basename(archive_path)
        archive_name = archive_fname.split('.')[0]
        folder = '/data/web_static/releases'
        run('mkdir -p {}/{}'.format(folder, archive_name))
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}'
            .format(archive_fname, archive_name))
        run('mv {0}/{1}/web_static/* {0}/{1}/'.format(folder, archive_name))
        run('rm /tmp/{}'.format(archive_fname))
        run('rm -rf /data/web_static/current')
        run('ln -s /data/web_static/releases/{}/ /data/web_static/current'
            .format(archive_name))
        print("New version deployed!")
        return True
    except Exception:
        return False
