#!/usr/bin/env python
# encoding: utf-8
# Copyright (C) 2015 Foxio
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

def options(opts):
    opts.load("compiler_c compiler_cxx")

def configure(conf):
    conf.load ("compiler_c compiler_cxx")

def build(bld):
    bld.install_files(bld.env.PREFIX + '/bin', bld.path.ant_glob('bin/*'), chmod=0755)
