#!/usr/bin/python3
""" pack web_static as archive """
from fabric.api import local
import datetime


def do_pack():
    """ pack as tgz archive """
    try:
        current_time = datetime.datetime.now()
        formatted = current_time.strftime("%Y%m%d%H%M%S")
        archive_name = "web_static_{}.tgz".format(formatted)
        local("mkdir -p ./versions")
        local("tar -cvzf ./versions/{} \
              ./web_static".format(archive_name))
        path = "versions" + archive_name
        return path
    except Exception:
        return None
