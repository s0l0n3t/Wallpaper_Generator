import urllib.request
import os
import time

file_path_number = 0
server_http = "http://source.unsplash.com/random/1920x1080"


def server_connect(connect_http_addr):
	global file_path_number
	file_path_number+=1
	file_path = personal_path+ os.sep + str(file_path_number)+".jpg"
	connect_server = urllib.request.urlopen(connect_http_addr)
	file_writer = open(file_path,"wb")
	#wb -->Binary şeklinde okuma 
	file_writer.write(connect_server.read())
	connect_server.close()
	time.sleep(2)
	file_writer.close()

personal_ = input("Number> ")
personal_path = input("Folder> ")
while True:
	if file_path_number != int(personal_): #istediğimiz miktarın bir fazlası.
		server_connect(server_http)
		
	else:
		break

