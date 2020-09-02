import mss
import numpy

class ColorFetcher:
    def __init__(self):
        self.monitor={'top':0,'left':0,'width':1920,'height':1080}
        self.sct=mss.mss()

    def getLatest(self):
        img=numpy.array(self.sct.grab(self.monitor))
        img=numpy.delete(img, 3,2)
        img=numpy.mean(img,axis=0)
        img=numpy.mean(img,axis=0)
        img=numpy.flip(img)
        img=numpy.rint(img)

        x_arrstr=numpy.char.mod('%d',img)
        return ",".join(x_arrstr)