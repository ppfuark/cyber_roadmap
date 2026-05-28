from scapy.all import sniff, IP

def packet_handler(packet):
    if IP in packet:
        print(f"Src: {packet[IP].src} -> Dst: {packet[IP].dst}")

sniff(prn=packet_handler, count=10, filter="ip")