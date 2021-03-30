import bluetooth

print("Procurando devices conectados...")
devices = bluetooth.discover_devices(lookup_names=True)

for addr, name in devices:
    print("Endereço: ", addr)
    print("Nome: ", name)