import socket
from concurrent.futures import ThreadPoolExecutor

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
    total_ports = portB - portA
    open_ports = []
    close_ports = []

    futures = []

    with ThreadPoolExecutor(max_workers=10) as executor:

        for port in range(portA, portB):

            future = executor.submit(scan_port, target, port)
            futures.append((port, future))

        for port, future in futures:
            result = future.result()

            if result:
                print(port, "Open Port")
                open_ports.append(port)
            else:
                print(port, "Closed Port")
                close_ports.append(port)

        print("----------------------------------------------------------------------")
        print("Total Ports: ", total_ports)
        print("Closed Ports: ", len(close_ports))
        print("Opened Ports: ", len(open_ports))

        print("Open Port List:", open_ports)




def main():
    scan_ports("127.0.0.1", 1, 9999)

main()