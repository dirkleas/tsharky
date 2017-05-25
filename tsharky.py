
#
# tsharky.py - minimal TShark wrapper to stream netword capture as OSC
#              messages. H4x IP/PORT and tshark args per preferences.
#
# Copyright (C) 2017 Dirk Leas
#
# This program is free software; you may redistribute and/or modify
# it under the terms of the GNU General Public Licence as published by
# the Free Software Foundation, either version 3 of said Licence, or
# (at your option) any later version.
#

import subprocess
from pythonosc import osc_message_builder, udp_client # python 3.3.x+

osc = udp_client.UDPClient('localhost', 8000)
popen = subprocess.Popen(['tshark', '-l'], stdout=subprocess.PIPE)
for traffic in iter(popen.stdout.readline, ''):
    traffic = traffic.decode('utf-8').strip()
    #print(traffic)
    msg = osc_message_builder.OscMessageBuilder(address='/tsharky')
    msg.add_arg(traffic, 's')
    msg = msg.build()
    osc.send(msg)

