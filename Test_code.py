import Faster_pycrafter6500
import numpy
import time
import PIL.Image

'''
generate = numpy.zeros((1080, 1920))
generate[:, 500:1500] = 1
'''


pic = numpy.asarray(PIL.Image.open("testimage.tif"))

t0 = time.clock()
encoded_data = Faster_pycrafter6500.generate_encoded(pic)


dlp=Faster_pycrafter6500.dmd()
dlp.stopsequence()
dlp.changemode(3)
exposure=[1000000]*30
dark_time=[0]*30
trigger_in=[False]*30
trigger_out=[1]*30
t2 = time.clock()
print("Configure and start DMD need:", t2-t1, 's')


dlp.defsequence(encoded_data,exposure,trigger_in,dark_time,trigger_out,0)
dlp.startsequence()
t3 = time.clock()
print("DMD update pattern need:", t3-t2, 's')