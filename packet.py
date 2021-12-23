import scapy.all as scapy
number_of_packets = 6
results = scapy.sniff(count=number_of_packets)
for i in range(0,number_of_packets):
	results[i].show()
