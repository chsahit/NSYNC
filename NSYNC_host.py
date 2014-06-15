#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  NSYNC_host.py
#  
#  Copyright 2014 sc <sc@sc-chaos>
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

dbname = None #name of the database file
tablename = None #name of the table being synced
portnum = None # the port that the client will connect to the host on

import socket
import sys
import sqlite3 as sql

EOT = "\4" #ASCII End Of Transmission character
ETB  = "\23" #ASCII End Trans. Block character
US = "\31" #ASCII Unit Separator character
def main():
	dbname = sys.argv[1] #path to the db file
	tablename = sys.argv[2] #name of the table being synced
	portnum = int(sys.argv[3]) #port that client will connect to host on
	syncing = True
	
	client_socket = connect_to_client(portnum)
	db_con = sql.connect(dbname)
	try:
		cursor = db_con.cursor()
		print "syncing..."
		while(syncing):
			element = get_data(client_socket)
			if(element == EOT):
				syncing = False
			else:
				values = parse_data(element)
				update_table(tablename,values)
			
def connect_to_client(portnumber):	
	pass
	
def get_data(sock):
	pass
	
def parse_data(raw_data):
	pass
	
def update_data(values):
	pass
	
if __name__ == '__main__':
	main()

