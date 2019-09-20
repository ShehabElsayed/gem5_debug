# -*- coding: utf-8 -*-
# Copyright (c) 2016 Jason Lowe-Power
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met: redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer;
# redistributions in binary form must reproduce the above copyright
# notice, this list of conditions and the following disclaimer in the
# documentation and/or other materials provided with the distribution;
# neither the name of the copyright holders nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
# Authors: Jason Lowe-Power

#from system import MySystem

import m5
from m5.util import addToPath

addToPath('../')
from common import SimpleOpts

SimpleOpts.add_option("--script", default='',
                      help="Script to execute in the simulated system")

SimpleOpts.add_option("--no_host_parallel", default=False, action="store_true",
            help="Do NOT run gem5 on multiple host threads (kvm only)")

SimpleOpts.add_option("--num_cpus", default=2, type="int",
                      help="Number of CPUs in the system")

SimpleOpts.add_option("--second_disk", default='',
                      help="The second disk image to mount (/dev/hdb)")

SimpleOpts.add_option("--enable_tuntap", action='store_true',
                      default=False, help="")

SimpleOpts.add_option("--l2_size", default="256kB", help="L2 size")

#FIXME: set in run script
SimpleOpts.add_option("--num_l2caches", default=1,
            help="Number of L2 cache banks")

SimpleOpts.add_option("--cacheline_size", default=64,
            help="Cache block size in B")

SimpleOpts.add_option("--l1i_size", default="64kB", help="L1I size")

SimpleOpts.add_option("--l1i_assoc", default=2, help="L1I associativity")

SimpleOpts.add_option("--l1d_size", default="64kB", help="L1D size")

SimpleOpts.add_option("--l1d_assoc", default=2, help="L1D associativity")

SimpleOpts.add_option("--l2_assoc", default=8, help="L2 associativity")

#FIXME: set in run script
SimpleOpts.add_option("--num_dirs", default=1, help="Number of directories")

SimpleOpts.add_option("--mem_type", default="DDR3_1600_8x8",
            help="Main memory type")

SimpleOpts.add_option("--enable_dram_powerdown", default=False,
            help="Enable DRAM power down")
