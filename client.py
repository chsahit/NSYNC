#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  client.py
#  
#  Copyright 2014 Sahit Chintalapudi <chsahit@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import socket
#A test client file to make sure host is working
#TODO client.py that turns a table into data which can be sent over the socket
def main():
		sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		sock.connect(("localhost",portnum))
		sock.send("rowval\31colvalue\23\4")

if __name__ == '__main__':
	main()

