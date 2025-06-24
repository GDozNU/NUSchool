import socket
import time

def scan_ports(target, start_port, end_port):
    print(f"\nScanning {target} from port {start_port} to {end_port}...\n")

    # Validate port range
    if start_port < 0 or end_port > 65535 or start_port > end_port:
        print("Invalid port range. Ports must be between 0 and 65535.")
        return

    for port in range(start_port, end_port + 1):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"Port {port} is OPEN")
            else:
                print(f"Port {port} is CLOSED")
            sock.close()
        except socket.gaierror:
            print("Hostname could not be resolved.")
            break
        except socket.error:
            print("Could not connect to server.")
            break

        time.sleep(0.1) 


try:
    # 1. Normal scan on common ports
    scan_ports('127.0.0.1', 20, 25)

    # 2. Invalid port range
    scan_ports('127.0.0.1', -5, 10)

    # 3. Scan port 65432 (should be open if server.py is running I think)
    scan_ports('127.0.0.1', 65432, 65432)

    # 4. Scan scanme.nmap.org (Using IPV4 address)
    scan_ports('45.33.32.156', 20, 25)


except Exception as e:
    print(f"Scan failed: {e}")

