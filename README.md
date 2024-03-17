# Python Projects

# scanner.py
Is a simple network scanner script that uses the `scapy` library to ping IP addresses within a specified subnet and identify active hosts. It provides two functions: `ping_host` and `scan_network`.

The `ping_host` function sends an ICMP echo request (ping) to a single IP address and returns `True` if the host responds, or `False` otherwise.

The `scan_network` function takes a list of IP addresses and calls `ping_host` for each address. It prints the IP addresses of active hosts and returns a list of active host IPs.

The script uses the `ipaddress` module to generate a list of all IP addresses within a specified subnet (e.g., "11.28.0.0/24"). It then calls the `scan_network` function with this list and prints the number of active hosts found.

Overall, this script can be used to quickly scan a local network subnet and identify active hosts, which can be useful for network inventory, troubleshooting, or security purposes.

You will need to run the script with "Sudo/Admin" Privileges.
