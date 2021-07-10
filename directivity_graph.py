import numpy as np
import matplotlib.pyplot as plt

# Reference values in 0.txt for each selected frequency
ref0 = []
freq, magnitude0, phase, coherence = np.loadtxt("data/0.txt", unpack=True)
ref0.append(magnitude0[53:775]) #it takes all frequency values from 62.5 to 16k

matrixOld = []
for i in range(-90,105,15):
    freq, magnitude, phase, coherence = np.loadtxt("data/" + str(abs(i)) + ".txt", unpack=True)
    matrixOld.append(magnitude[53:775])

# Normalization
n_matrix = np.array(matrixOld) - np.array(ref0)

# Plot Config
Y = np.arange(-90,105,15) 

freqs = np.array([62.5,125,250,500,1000,2000,4000,8000,16000])
freq_label = ["62.5","125","250","500","1k","2k","4k","8k","16k"]
degrees = np.array(np.arange(-90,105,15))

f = freq[53:775]

# Plot
fig, ax = plt.subplots (1, 1)
cp = ax.contourf(f, Y, n_matrix, 20, cmap=plt.get_cmap('jet'))
# cp = ax.contourf(f, Y, matrixOld, 20, cmap=plt.get_cmap('jet'))
plt.colorbar (cp, label='[dBFS]', ticks = range(-40,1,2))
plt.minorticks_on()
plt.semilogx()
plt.grid(color='black')
plt.xticks(freqs, list(freqs))
ax.set_xticklabels(freq_label,rotation=45)
plt.yticks(degrees, list(degrees))
plt.title('Directividad horizontal referida al eje.')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Ángulo de Incidencia [°]')
plt.show()