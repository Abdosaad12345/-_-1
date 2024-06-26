
from scapy.all import sniff
from scapy.all import IP, Ether

def packet_handle(packet):
    if Ether in packet and IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        packet_size = len(packet)
        
        protocol = packet[IP].fields.get('proto', 'Unknown')
        
        print(f"Source IP: {src_ip}, Destination IP: {dst_ip}, Protocol: {protocol}, Packet size: {packet_size}")

sniff(prn=packet_handle, count=50)
