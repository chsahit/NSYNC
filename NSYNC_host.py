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
	
	client_socket = connect_to_client('localhost',portnum)
	db_con = sql.connect(dbname)
	try:
		cursor = db_con.cursor() #used to manipulate tables in the db
		print "syncing..."
		while(syncing):
			element = get_data(client_socket)
			if(element == EOT): #the last message was sent
				syncing = False
			else:
				values = parse_data(element) #the list of new vals
				update_table(tablename,values)
				
#takes an open port and returns socket to client			
def connect_to_client(portnumber):	
	server_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	server_sock.bind(("localhost",portnumber))
	server_sock.listen(5) #TODO Pick a number
	(clientsocket,address) = server_sock.accept()	
	return clientsocket
	
#reads each trans. block from the client and returns it
#reads one byte at a time until ETB is sent
def get_data(sock):
	data = ""
	while(True) :
		curr_char = sock.recv(1)
		if(thisChar == ETB):
			break
		else :
			message = message + curr_char
	return message
	
def parse_data(raw_data):
	values = []
	unit_separator = raw_data.find("\31")
	if(unit_separator == -1):
		values.append(raw_data)
		return values
	values.append(parse_data(raw_data[unit_separator+1:]))
	values.append(raw_data[:unit_separator])
	values.reverse()
	return values
	
def update_data(values):
	pass
	
if __name__ == '__main__':
	main()

