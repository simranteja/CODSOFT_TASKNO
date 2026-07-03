




from scapy.all import sniff, IP, IPv6, TCP, UDP, ICMP

def packet_callback(packet):
    print("=" * 60)

    # IPv4 Packets
    if IP in packet:
        print(f"Source IP      : {packet[IP].src}")
        print(f"Destination IP : {packet[IP].dst}")

    # IPv6 Packets
    elif IPv6 in packet:
        print(f"Source IP      : {packet[IPv6].src}")
        print(f"Destination IP : {packet[IPv6].dst}")

    # Protocol Detection
    if TCP in packet:
        print("Protocol       : TCP")
    elif UDP in packet:
        print("Protocol       : UDP")
    elif ICMP in packet:
        print("Protocol       : ICMP")
    else:
        print("Protocol       : Other")

    print(f"Packet Length  : {len(packet)} bytes")
    print("-" * 60)
    print(packet.summary())

print("=" * 60)
print("      Network Packet Analyzer Started")
print("      Press Ctrl + C to Stop")
print("=" * 60)

sniff(prn=packet_callback, store=False)