#!/usr/bin/env python
# encoding: utf-8
# Copyright (C) 2015-2016 Foxio
# Author Michael Fisher <mike@fox.io>

''' This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public Licence as published by
the Free Software Foundation, either version 3 of the Licence, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
file COPYING for more details. '''

import os, sys
sys.path.insert (0, os.getcwd())
import rails
from subprocess import call

# Required by waf
top = '.'
out = 'build'

def options (opts):
    opts.add_option('--rails-version', default='5.0.0.1', dest='rails_version', type='string', \
        help="Specify the Rails Version [Default: 5.0.0.1]")
    opts.add_option('--ruby-version', default='2.2.5', dest='ruby_version', type='string', \
        help="Specify the Rails Version [Default: 2.2.5]")
    opts.add_option('--docker-tag', default='latest', dest='docker_tag', type='string', \
        help="Specify the Rails Version [Default: latest]")

def configure (conf):
    conf.find_program('docker', mandatory=True)
    conf.find_program('docker-compose', mandatory=False)
    conf.env.RAILS_VERSION = conf.options.rails_version
    conf.env.RUBY_VERSION = conf.options.ruby_version
    conf.env.DOCKER_TAG = conf.options.docker_tag

    print
    rails.display_header ('Rails Image Configuration')
    rails.display_msg (conf, 'Ruby Version', conf.env.RUBY_VERSION)
    rails.display_msg (conf, 'Rails Version', conf.env.RAILS_VERSION)
    rails.display_msg (conf, 'Docker Tag', 'foxio/rails:%s' % conf.env.DOCKER_TAG)

def build_image (bld):
    call(['docker', 'build', '-f', 'build/Dockerfile', \
                             '-t', 'foxio/rails:%s' % bld.env.DOCKER_TAG, \
                             '.'])

def build (bld):
    bld (
        features = 'subst',
        source = 'Dockerfile.in',
        target = 'Dockerfile',
        rails_version = bld.env.RAILS_VERSION,
        ruby_version = bld.env.RUBY_VERSION
    )

    bld.add_post_fun (build_image)
    bld.install_files(bld.env.PREFIX + '/bin', bld.path.ant_glob('bin/*'), chmod=0755)
