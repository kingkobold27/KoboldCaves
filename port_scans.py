import socket
from concurrent.futures import ThreadPoolExecutor
import time
import ipaddress
import errno
from server_ports import get_service_name

def scan_port(target, port):
    # Notes for me:
        #AF_INET selects the IPv4 Family for ips
        #SOCK_STREAM selects a socket stream, normally with TCP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        #with function closes the connection automatically after the function reaches its end
        sock.settimeout(1)
        #timeout is how long it will take before it gives up with recieving no response for this its only a second
        #does not account for network errors or other conditions: might change to higher number

        result = sock.connect_ex((target, port))
        #creates TCP connection to the address and the port which i want to connect

        if result == 0:
        #returns if the it connection works (opened vs closed)
            return "open"
        elif result == errno.ECONNREFUSED:
            return "closed"
        else:
            return "filtered_or_error"
       
        
 

def scan_ports(target, portA, portB):
    total_ports = portB - portA
    #total ports = portB # - portA #
    open_ports = []
    #empty array for opened ports
    closed_ports = []
    #empty array for closed ports
    other_ports = []

    futures = []
    #empty array for tuples to be added


    start_time = time.perf_counter()
    #start recording time
    with ThreadPoolExecutor(max_workers=10) as executor:
        #create 10 workers with thread executor
        for port in range(portA, portB):
            #for port in the range defined in the calling of the function (portA, portB)
            future = executor.submit(scan_port, target, port)
            #define what one future is (executor.submit(scan_port, target, port))
            #executor.submit functions by naming the function and the variables for that function
            #then it submits that function to the executor to send in order
            futures.append((port, future))
            #add tuple of port and future to the list of futures

        for port, future in futures:
            #for each future in futures, a single future is submit to the executor
            result = future.result()
            #the result is the the future's result of the execute, in this case the scan_port function

            if result == "open": #IF TRUE 
                print(port, "Open Port")
                open_ports.append(port)
                #print the port, that it is open, and append the port to the open_ports array
            elif result == "closed":
                closed_ports.append(port)
                #closed ports added to closed_ports array
            else:
                other_ports.append(port)

    elapsed_time = time.perf_counter() - start_time
    #time it took to do the process and below prints it
    print("\nScan Duration:", round(elapsed_time, 2), "seconds")

    print("--------------------------- Scan Results ---------------------------")
    print("Total Ports Scanned: ", total_ports)
    print("Range: ", portA, "-", portB-1)
    print("Closed Ports: ", len(closed_ports))
    print("Opened Ports: ", len(open_ports))
    print("Filtered or Error Ports: ", len(other_ports))


    print("Open Port List:", open_ports)

    ans = input("Would the user like to see the open services? (y/n) ")
    if ans.lower() == "y":
        for p in open_ports:
            print(p, get_service_name(p))
            

    ans = input("Would the user like to see the closed ports (y/n) ")
    if ans.lower() == "y":
        print(closed_ports)

    ans = input("Would the user like to see the filtered or errored ports? (y/n) ")
    if ans.lower() == "y":
        print(other_ports)
    
    
    print("\nGoodbye!")    
    

def interactive():
    
    while True:
        ip = input("Enter IP to scan: ")
        try:
            ipaddress.IPv4Address(ip)
            break
        except ValueError:
            print("Invalid IP Address")
            continue
    while True:

        while True:
            try:
                port1 = int(input("Enter the port you want to start scanning from: "))
                break
            except ValueError:
                print("Port must be an Integer")
                continue
        while True:
            try:
                port2 = int(input("Enter the port you want to stop scanning at: "))
                break
            except ValueError:
                print("Port must be an Integer")
                continue
        #asks for the IP and port range
        if 1 <= port1 <= 65535 and 1 <= port2 <= 65535 and port1 < port2:
            #checks that the port numbers are in the acceptable range and that port 1 is smaller than port 2
            break 
        else:
            print("Port Range is Invalid.")
            #if ports not valid 
            continue
                
    scan_ports(ip, port1, port2)
    #run scan_ports



#def main():
#   interactive()
#run it
#main()