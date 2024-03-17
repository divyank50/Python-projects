from scapy.all import ICMP, IP, sr1, sr, conf
import ipaddress

def ping_host(ip):
    """
    Sends an ICMP echo request (ping) to the specified IP address.
    Returns True if the host responds, False otherwise.
    """
    # Disable verbosity of scapy
    conf.verb = 0
    
    packet = IP(dst=ip)/ICMP()
    reply = sr1(packet, timeout=2)
    
    if reply:
        return True
    else:
        return False

def scan_network(ip_list):
    """
    Scans a list of IP addresses, pinging each to identify active hosts.
    """
    active_hosts = []
    for ip in ip_list:
        if ping_host(ip):
            print(f"Host up: {ip}")
            active_hosts.append(ip)
    return active_hosts

# Example usage
if __name__ == "__main__":
    # Define the subnet to scan (e.g., "11.28.0.1/24")
    subnet = "11.28.0.0/24"
    network = ipaddress.ip_network(subnet)
    
    # Generate all IP addresses in the subnet
    ip_addresses = [str(ip) for ip in network.hosts()]
    
    print("Starting scan...")
    active_hosts = scan_network(ip_addresses)
    print(f"Scan completed. Active hosts: {len(active_hosts)}")
