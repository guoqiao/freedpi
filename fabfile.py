# -*- coding: UTF-8 -*-
from fabric.api import *
env.use_ssh_config = True
env.hosts = ['rf']
env.proj_root = '/srv/src/freedpi'

def pull():
    with cd(env.proj_root):
       run("git pull")
       run("jekyll build")
