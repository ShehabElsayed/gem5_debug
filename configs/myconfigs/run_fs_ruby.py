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

""" Script to run a workload in KVM with gem5
    When this script is run without the --script parameter, gem5 will boot
    Linux and sit at the command line, assuming this is how your disk is
    configured. With the script parameter, the script will be executed on the
    guest system.

    If your application has ROI annotations, this script will count the total
    number of instructions executed in the ROI. It also tracks how much
    wallclock and simulated time.
"""

import sys
import time

import m5
import m5.ticks
from m5.objects import *
from m5.util import addToPath

addToPath('../') # For the next line...
from common import SimpleOpts

from system.system_ruby import MyRubySystem

#SimpleOpts.add_option("--script", default='',
#                      help="Script to execute in the simulated system")
#SimpleOpts.add_option("--cpus", default='',
#                      help="Script to execute in the simulated system")

if __name__ == "__m5_main__":
    print(sys.argv)
    #(opts, args) = SimpleOpts.parse_args()

    # create the system we are going to simulate
    system = MyRubySystem()
    (opts, args) = SimpleOpts.parse_args()
    system.createMyRubySystem(opts, no_kvm = False)

    # For workitems to work correctly
    # This will cause the simulator to exit simulation when the first work
    # item is reached and when the first work item is finished.
    system.work_begin_exit_count = 1
    system.work_end_exit_count = 1

    # Read in the script file passed in via an option.
    # This file gets read and executed by the simulated system after boot.
    # Note: The disk image needs to be configured to do this.
    system.readfile = opts.script

    # set up the root SimObject and start the simulation
    root = Root(full_system = True, system = system,
                time_sync_enable = True, time_sync_period = '1000us')

    if system.getHostParallel():
        # Required for running kvm on multiple host cores.
        # Uses gem5's parallel event queue feature
        # Note: The simulator is quite picky about this number!
        root.sim_quantum = int(1e9) # 1 ms

    # instantiate all of the objects we've created above
    m5.instantiate()

    globalStart = time.time()

    print("Running the simulation")
    exit_event = m5.simulate()

    num_exits = 0

    while num_exits != 1:
        print("exited because", exit_event.getCause())

        if exit_event.getCause() == "m5_exit instruction encountered":
            num_exits = num_exits + 1
            system.switchCpus(system.cpu, system.o3Cpu)

        # If the user pressed ctrl-c on the host, then we really should exit
        if exit_event.getCause() == "user interrupt received":
            print("User interrupt. Exiting")
            break

        print("Continuing")
        exit_event = m5.simulate()

    print("Normally exiting simualtion")
