import socket
from concurrent.futures import ThreadPoolExecutor
import time

def scan_port(target, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(1)

        result = sock.connect_ex((target, port))

        return result == 0
       
        
 

def scan_ports(target, portA, portB):
    total_ports = portB - portA
    open_ports = []
    closed_ports = []

    futures = []

    start_time = time.perf_counter()
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
                closed_ports.append(port)

    elapsed_time = time.perf_counter() - start_time
    print("\nScan Duration:", round(elapsed_time, 2), "seconds")

    print("--------------------------- Scan Results ---------------------------")
    print("Total Ports Scanned: ", total_ports)
    print("Range: ", portA, "-", portB-1)
    print("Closed Ports: ", len(closed_ports))
    print("Opened Ports: ", len(open_ports))

    print("Open Port List:", open_ports)
    

def interactive():
    
    while True:
        ip = input("Enter IP to scan: ")
        port1 = int(input("Enter the port you want to start scanning from: "))
        port2 = int(input("Enter the port you want to stop scanning at: "))
        if 1 <= port1 <= 65535 and 1 <= port2 <= 65535 and port1 < port2:
            break
        else:
            print("Invalid Argument. Out of Port Range.")
            continue
            
    scan_ports(ip, port1, port2)



def main():
    interactive()

main()