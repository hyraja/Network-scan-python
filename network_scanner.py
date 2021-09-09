#!/usr/bin/python3

# Menu driven network scanning tool:
import nmap
import sys
# import popen
import os


def main_menu():
    print("1.Get device details")
    print("2.Scan the network for open port")
    print("3.Scan single host ")
    print("4.Scan range")
    print("5.Aggressive scan")
    print("6.Scan ARP packet")
    print("7.Scan all port only")
    print("8.Scan in verbose mode")
    print("9.Exit")


while True:
    main_menu()
    ch = int(input("Enter choice: "))
    nm = nmap.PortScanner()  # Create object of nmap port scannet class
    # nm = nmap.PortScanner()

    print("Wait.......................")
    # Returns Dictinary
    # ip = input("Enter the IP : ")
    ip = str(sys.argv[1])
    # rangel = input('Enter range like 1-2000 : ')
    rangel = str(sys.argv[2])
    # interface = input("Enter interface : like -v -sS -O -e enp0s3 : ")
    # -v --> for verbose output
    verbose = sys.argv[3]
    # -s for scan
    s = sys.argv[4]
    # p --> ping scan ,looks like -sp
    # S -- > stleath scan
    # V -- > version scan
    # L --> list scan
    scanp = sys.argv[5]
    cmd = str(s+scanp)
    # -O --> os scan
    oss = str(sys.argv[6])
    # -e --> for interface name
    mis = str(sys.argv[7])
    # for interface name
    inter = str(sys.argv[8])
    # ### -A --> Aggressive scan
    # aggr = sys.argv[9]

    os_command = ' '.join([x for x in [verbose, cmd, oss, mis, inter]])

    def result():

        hostname = f"Hostname : {scan['scan'][ip]['hostnames']}"
        address = f" Address : {scan['scan'][ip]['addresses']}"
        status = f"status : {scan['scan'][ip]['status']}"

        print(hostname, address, status, end='\n')
        for port in scan['scan'][ip]['tcp'].items():
            print(
                f"{port[0]}, state : {port[1]['state']},name : {port[1]['name']},reason : {port[1]['reason']},Product : {port[1]['product']},version : {port[1]['version']},conf: {port[1]['conf']},cpe : {port[1]['cpe']}")

    if ch == 1:

        try:

            scan = nm.scan(ip, rangel, os_command)
            print(f'Command : {nm.command_line()}')
            # print(f" scan Info : {nm.scaninfo()}")
            result()
        except:
            print("Use root priviliege")
    elif ch == 2:
        # nm = nmap.PortScanner()  # create object of nmap port scanner class

        try:

            scan = nm.scan(ports=rangel, arguments=os_command)
            # print(scan)
            print(f'Command : {nm.command_line()}')
            # print("scan Info : ", nm.scaninfo())
            result()
        except:
            print("Use root priviliege")

        # print(scan)
    elif ch == 3:
        # scan single host
        try:
            scan = nm.scan(ip)
            print(f'Command : {nm.command_line()}')
            # print("scan Info : ", nm.scaninfo())
            # print(scan)
            result()
        except:
            print("use root privililage")
    elif ch == 4:
        # scan range
        try:

            scan = nm.scan(ip, rangel)
            print(f'Command : {nm.command_line()}')
            # print("scan Info : ", nm.scaninfo())
            # print(scan)
            result()
        except:
            pass
    elif ch == 5:
        nmapip = "nmap -A " + ip
        scan = os.system(nmapip)
        # nmap - sp 192.168.1.1/24
        print(scan)
    elif ch == 6:
        # nmap 192.168.1.0/24 - PR
        nmap_ip = "nmap " + ip + " -PR"
        scan = os.system(nmap_ip)
        print(scan)
    elif ch == 7:
        nmap_ip = "nmap -Pn " + ip
        scan = os.system(nmap_ip)
        print(scan)
    elif ch == 8:
        nmap_ip = "nmap -v " + ip
        scan = os.system(nmap_ip)
        print(scan)
    elif ch == 9:
        break
    else:
        print("Wrong Choice")
