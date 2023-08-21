import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

x = np.arange(0,4,0.05)
y = np.sin(x*np.pi)

ax.plot(x,y)
ax.set_xlabel('time (seconds)')
ax.set_ylabel('Amplitude (Volts)')
ax.set_title('Sine wave for two periods')
fig.set_facecolor('green')

ax.grid(visible=True)
plt.show()