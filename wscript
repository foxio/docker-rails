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

import sys
from subprocess import call

# Required by waf
top = '.'
out = 'build'

def options (opts):
    opts.add_option('--rails-version', default='4.2.5', dest='rails_version', type='string', \
        help="Specify the Rails Version [Default: 4.2.5]")
    opts.add_option('--ruby-version', default='2.2.3', dest='ruby_version', type='string', \
        help="Specify the Rails Version [Default: 2.2.3]")

def configure (conf):
    conf.env.RAILS_VERSION = conf.options.rails_version
    conf.env.RUBY_VERSION = conf.options.ruby_version

def build_image (bld):
    call(['docker', 'build', '-f', 'build/Dockerfile', \
                             '-t', 'foxio/rails', '.'])

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
