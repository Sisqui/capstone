import numpy as np
import scipy.io.wavfile as wav
from scipy import signal
import matplotlib.pyplot as plt
from pylab import specgram
import os
import os.path
import cv2


#audiopath='Recordings/3D + small mic 6.wav'
audiopath='sound/crackles_a.wav'
filename=audiopath[11:-4]
samplerate,sample = wav.read(audiopath)
if(sample.ndim>1):#scipy.io.wavfile
    sample=sample[:,0]
seconds=len(sample)/samplerate
if seconds<7:
    exit("audio too short")
result=specgram(sample, NFFT=256, Fs=samplerate, noverlap=64) #from pylab
spec,frqs,times=result[0],result[1],result[2]
print(seconds)
print(spec.shape)
#spec=np.array(spec)
#cv2.plot(spec)
f=open('recording.txt','w+')
while (1):
    i=input()
    if i=='e':
        break
    tag=input()
    n =abs(spec[8:, int(i)])
    n=n/max(n)
    a=[]
    for i in n:
        a.append(str(i))
    str1=",".join(a)
    str2=','+str(tag)+'\n'
    str1+=str2
    f.write(str1)
f.close()


