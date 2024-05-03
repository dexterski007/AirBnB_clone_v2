#!/usr/bin/python3
""" clean archives """
from fabric.api import *


env.hosts = ['100.25.41.53', '52.3.253.7']
env.user = "ubuntu"


def do_clean(number=0):
    """ cleaning archives """

    number = int(number)

    if number == 0:
        number = 2
    else:
        number += 1

    local('cd versions ; ls -t | tail -n +{} | xargs rm -rf'.format(number))
    path = '/data/web_static/releases'
    run('cd {} ; ls -t | tail -n +{} | xargs rm -rf'.format(path, number))
