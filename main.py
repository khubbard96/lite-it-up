from DeviceConnection2 import DeviceConnection
from ColorFetcher import ColorFetcher
import time

conn = DeviceConnection("/dev/cu.usbserial-1410",9600)
numLEDS = conn.getLEDCount()
print(numLEDS)
fetcher = ColorFetcher()

while True:
    rgbStr = fetcher.getLatest()
    #print(rgbStr)
    for led in range(int(numLEDS)):
        packetToSend = "<" + str(led) +","+ rgbStr + ">"
        print(packetToSend)
        conn.sendPacket(packetToSend)
    time.sleep(1)

#print (str(conn.isDeviceConnected()))