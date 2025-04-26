# port_scanner.py

import socket
import sys
from concurrent.futures import ThreadPoolExecutor

# ANSI color codes
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

# Function to grab banner from open port
def get_banner(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        sock.connect((ip, port))
        banner = sock.recv(1024).decode().strip()
        sock.close()
        return banner
    except:
        return ""

# Function to scan a single port
def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            try:
                service = socket.getservbyport(port)
            except:
                service = "Unknown"
            banner = get_banner(ip, port)
            return (port, service, banner)
    except:
        pass
    return None

# Function to format and print the results
def format_port_results(results):
    print(f"\n{GREEN}{'PORT':<10} {'SERVICE':<15} {'BANNER':<30}{RESET}")
    print("-" * 60)
    for port, service, banner in results:
        print(f"{GREEN}{port:<10} {service:<15} {banner:<30}{RESET}")

# Main port scanning function
def port_scan(target, start_port, end_port):
    try:
        ip = socket.gethostbyname(target)
    except socket.gaierror:
        print(f"{RED}[-] Unable to resolve hostname {target}.{RESET}")
        return

    print(f"\n[*] Starting scan on {ip} from port {start_port} to {end_port}...\n")
    open_ports = []

    with ThreadPoolExecutor(max_workers=100) as executor:
        futures = []
        for port in range(start_port, end_port + 1):
            futures.append(executor.submit(scan_port, ip, port))

        for i, future in enumerate(futures):
            sys.stdout.write(f"\rScanning port: {start_port + i}/{end_port}")
            sys.stdout.flush()
            result = future.result()
            if result:
                open_ports.append(result)

    format_port_results(open_ports)

# Entry point
if __name__ == "__main__":
    target = input("Enter target host (IP or domain): ")
    start_port = int(input("Enter starting port: "))
    end_port = int(input("Enter ending port: "))

    port_scan(target, start_port, end_port)
