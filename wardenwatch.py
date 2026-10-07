import socket


def scan_port(target, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    result = sock.connect_ex((target, port))

    sock.close()

    if result == 0:
        return True
    else:
        return False
        
 

def scan_ports(target, portA, portB):
    totalPorts = portB - portA
    open_ports = []
    close_ports = []

    for port in range(portA, portB):

        result = scan_port(target, port)

        if result:
            print(port, "Open Port")
            open_ports.append(port)
        else:
            print(port, "Closed Port")
            close_ports.append(port)

    print("----------------------------------------------------------------------")
    print("Total Ports: ", totalPorts)
    print("Closed Ports: ", len(close_ports))
    print("Opened Ports: ", len(open_ports))

    print("Open Port List:", open_ports)




def main():
    scan_ports("127.0.0.1", 1, 9999)

main()