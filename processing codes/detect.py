from sklearn.tree import DecisionTreeClassifier
import pickle
file1=open('model.data','r')
clf=pickle.load(file1)

import scipy.io.wavfile as wav
from pylab import specgram
import peakutils


audiopath='sound/A1.wav'
#audiopath='sound/Inspiratory stridor.wav'
filename=audiopath[11:-4]
samplerate,sample= wav.read(audiopath)
#sample.reshape([22050,len(sample)/22050])
#print(samplerate)
if(sample.ndim>1):#scipy.io.wavfile
    sample=sample[:,0]
seconds=len(sample)/samplerate
if seconds<7:
    exit("audio too short")
result=specgram(sample, NFFT=256, Fs=samplerate, noverlap=64)
spec,frqs,times=result[0],result[1],result[2]

count=0
flag=0
for i in range(0,len(spec[0])):#range (len(spec[0])):
    cb=abs(spec[5:,i])
    loc=peakutils.indexes(cb, thres=0.02 * max(cb), min_dist=0)
    peaks=cb[loc]
    peak=cb[0]
    sum=0
    for k in range(0,int(len(peaks)/2)):
        sum=sum+abs(peaks[k])
    if sum/peak>5:
        count=count+1
#print(count)
if count>90:
    sum = 0
    for i in range(len(spec)):
        n = abs(spec[8:, int(i)])
        n = n / max(n)
        y_i = clf.predict(n.reshape(1, -1))
        if (y_i == '1'):
            sum += 1
    # print(sum)
    # print(len(spec))
    if float(sum) / float(len(spec)) > 0.3:
        print("crackles")
    else:
        print("healthy")
else:
    count1=0
    flag1=0
    for i in range(0,len(spec[0])):
        cb=abs(spec[5:,i])
        loc=peakutils.indexes(cb, thres=0.02 * max(cb), min_dist=0)
        peaks=cb[loc]
        peak=cb[0]
        for k in range(0,len(peaks)):
            if (peaks[k]>0.4*peak):
                if flag1==1:
                    count1=count1+1
                flag1=1
                break
            else:
                flag1=0
    #print(count1)
    if(count1>6):
        print('wheezes')
    else:
        print('crackles')

