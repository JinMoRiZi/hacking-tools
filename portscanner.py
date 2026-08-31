import socket
import threading

target = "192.168.133.129"
open_ports = []

def scan_port(port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.settimeout(1)
	result = s.connect_ex((target, port))
	if result == 0:
		try:
			service = socket.getservbyport(port)
		except:
			service = "unknown"
		try:
			banner = s.recv(1024).decode().strip().split("\n")[0]
			if not banner:
				s.sand(b"HEAD /HTTP/1.0\r\n\r\n")
				banner = s.recv(1024).decode().strip().split("\n")[0]
		except:
			banner = "no banner"
		open_ports.append((port, service, banner))
	s.close()

threads = []
for port in range(1, 1025):
	t = threading.Thread(target=scan_port, args=(port,))
	threads.append(t)
	t.start()

for t in threads:
	t.join()

print(f"scannimg {target}...\n")
for port, service, banner in sorted(open_ports):
	print(f"Port {port} | {service} | {banner}")


print("\nscan complet.")
