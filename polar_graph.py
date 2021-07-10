import numpy as np
import matplotlib.pyplot as plt

# Initialization of lists
# polar3125 = [] # 31,25 Hz => don't make sense because fs = 55 Hz
polar625 = [] # 62,5 Hz
polar125 = []

polar250 = []
polar500 = []
polar1k = []

polar2k = []
polar4k = []
polar8k = []
polar16k = []

# ref_3125 = []
ref_625 = []
ref_125 = []
ref_250 = []
ref_500 = []
ref_1k = []
ref_2k = []
ref_4k = []
ref_8k = []
ref_16k = []

# Reference values in 0.txt for each selected frequency
freq, magnitude0, phase, coherence = np.loadtxt("data/0.txt", unpack=True)
# ref_3125.append(magnitude0.item(21)) 
ref_625.append(magnitude0.item(53))
ref_125.append(magnitude0.item(117)) 
ref_250.append(magnitude0.item(188))
ref_500.append(magnitude0.item(259))
ref_1k.append(magnitude0.item(330))
ref_2k.append(magnitude0.item(442))
ref_4k.append(magnitude0.item(517))
ref_8k.append(magnitude0.item(667))
ref_16k.append(magnitude0.item(775))

# This for statement is used to load the files and consider them as symmetric
# It means that the measures of -90 = 90, -75 = 75, -60 = 60 and so on. 
for i in range(-90,105,15):
    freq, magnitude, phase, coherence = np.loadtxt("data/" + str(abs(i))+".txt", unpack=True)
    # polar3125.append(magnitude.item(21)) # index of the measure in txt 
    polar625.append(magnitude.item(53))
    polar125.append(magnitude.item(117)) 
    polar250.append(magnitude.item(188))
    polar500.append(magnitude.item(259))
    polar1k.append(magnitude.item(330))
    polar2k.append(magnitude.item(442))
    polar4k.append(magnitude.item(517))
    polar8k.append(magnitude.item(667))
    polar16k.append(magnitude.item(775))

# Normalizatiton
# n_polar3125 = np.array(polar3125) - np.array(ref_3125)
n_polar625 = np.array(polar625) - np.array(ref_625)
n_polar125 = np.array(polar125) - np.array(ref_125)
n_polar250 = np.array(polar250) - np.array(ref_250)
n_polar500 = np.array(polar500) - np.array(ref_500)
n_polar1k = np.array(polar1k) - np.array(ref_1k)
n_polar2k = np.array(polar2k) - np.array(ref_2k)
n_polar4k = np.array(polar4k) - np.array(ref_4k)
n_polar8k = np.array(polar8k) - np.array(ref_8k)
n_polar16k = np.array(polar16k) - np.array(ref_16k)

# Polar plot configuration
min_magnitude = -20
magnitude_res = 10

Y = np.arange(-90,105,15)                                                      
Y2 = Y * np.pi/180  

# 62,5 - 500 - 4k                                                           
fig = plt.figure()
ax = fig.add_subplot(111, projection="polar")
ax.plot(Y2,n_polar625, label="62,5 Hz")
ax.plot(Y2,n_polar500, label="500 Hz")
ax.plot(Y2,n_polar4k, label="4 kHz")
ax.set_theta_zero_location("N")
ax.set_thetagrids(Y)
ax.set_thetamin(-90)
ax.set_thetamax(90)
ax.set_rticks(range(min_magnitude,10,magnitude_res))
plt.legend(bbox_to_anchor=(1.01, 0.5), loc=3)
plt.title('Diagrama polar')
plt.show()

# 125 - 1k - 8k
fig = plt.figure()
ax = fig.add_subplot(111, projection="polar")
ax.plot(Y2,n_polar125, label="125 Hz")
ax.plot(Y2,n_polar1k, label="1 kHz")
ax.plot(Y2,n_polar8k, label="8 kHz")
ax.set_theta_zero_location("N")
ax.set_thetagrids(Y)
ax.set_thetamin(-90)
ax.set_thetamax(90)
ax.set_rticks(range(min_magnitude,10,magnitude_res))
plt.legend(bbox_to_anchor=(1.01, 0.5), loc=3)
plt.title('Diagrama polar')
plt.show()

# 250 - 2k - 16k
fig = plt.figure()
ax = fig.add_subplot(111, projection="polar")
ax.plot(Y2,n_polar250, label="250 Hz")
ax.plot(Y2,n_polar2k, label="2 kHz")
ax.plot(Y2,n_polar16k, label="16 kHz")
ax.set_theta_zero_location("N")
ax.set_thetagrids(Y)
ax.set_thetamin(-90)
ax.set_thetamax(90)
ax.set_rticks(range(min_magnitude,10,magnitude_res))
plt.legend(bbox_to_anchor=(1.01, 0.5), loc=3)
plt.title('Diagrama polar')
plt.show()