import pydbus
import os
print(f"DBUS_SYSTEM_BUS_ADDRESS={os.environ.get('DBUS_SYSTEM_BUS_ADDRESS')}")
try:
    print("Importing pydbus...")
    import pydbus
    print("Imported pydbus")
    print("Connecting to SystemBus...")
    bus = pydbus.SystemBus()
    print("Connected to bus")
    print("Listing names...")
    names = bus.dbus.ListNames()
    print(names)
except Exception as e:
    print(f"Error: {e}")
