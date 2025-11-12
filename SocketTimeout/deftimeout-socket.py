import socket
def socket_timeout():
	s = socket.socket()
	print('socket create successfully')
	print('Default socket timeout: '+ str(s.gettimeout()))
	
	s.settimeout(100)
	print('current socket timeout: '+ str(s.gettimeout()))

if __name__ == '__main__':

