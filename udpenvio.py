import socket

def envia_udp(enviar):
    UDP_IP = "192.168.1.100"
    UDP_PORT = 5005
    MESSAGE = enviar
     
    print "UDP target IP:", UDP_IP
    print "UDP target port:", UDP_PORT
    print "message:", MESSAGE
     
    sock = socket.socket(socket.AF_INET, # Internet
                          socket.SOCK_DGRAM) # UDP
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
