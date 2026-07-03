import socket

target = input("Enter IP to scan: ")
print(f"Scanning {target}")

for port in range(1, 101):  # Scans first 100 ports
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((target, port))
    if result == 0:
        print(f"Port {port} is OPEN")
    sock.close()

print("Scan complete")
