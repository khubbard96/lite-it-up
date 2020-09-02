import serial
import time

class DeviceConnection:
    def __init__(self, port, baudRate):
        self.deviceReady = False
        self.startMarker = 60
        self.endMarker = 62
        self.port = port
        self.baudRate = baudRate
        self.ser = serial.Serial(self.port, self.baudRate)

        msg = ""
        while msg.find("LEDS") == -1:
            while self.ser.inWaiting() == 0:
                pass

            msg = self._receive()

        #parse num LEDs
        self.numLEDs = msg.split(":")[1]

        msg=""
        while msg.find("READY") == -1:
            while self.ser.inWaiting() == 0:
                pass

            msg = self._receive()

        if(msg=="READY"):
            self.deviceReady = True
            print ("Device connection successful.")
        else:
            print ("Connection unsuccessful.")

    def _receive(self):
        ck = ""
        x = "z" # any value that is not an end- or startMarker
        byteCount = -1 # to allow for the fact that the last increment will be one too many
  
        # wait for the start character
        while  ord(x) != self.startMarker: 
            x = self.ser.read()
  
        # save data until the end marker is found
        while ord(x) != self.endMarker:
            if ord(x) != self.startMarker:
                ck = ck + x.decode("utf-8") 
                byteCount += 1
            x = self.ser.read()
        return(ck)

    def sendPacket(self, packet):
        packet = '{}'.format(packet).encode('cp1252')
        self.ser.write(packet)

    def isDeviceConnected(self):
        return self.deviceReady

    def getLEDCount(self):
        return self.numLEDs


