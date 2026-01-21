from scapy.all import get_if_list, get_if_hwaddr

print("\n--- NETWORK INTERFACES ---\n")

for iface in get_if_list():
    try:
        mac = get_if_hwaddr(iface)
        print(iface, " --> ", mac)
    except:
        pass

input("\nPress Enter to exit...")
