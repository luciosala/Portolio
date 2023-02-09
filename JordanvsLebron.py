import matplotlib.pyplot as plt
import numpy as np
## A very famous debate in sports is about who is better in Michael Jordan or Lebron James.In this graphic I show the points per game of both in their carreers
lebron_ppg = np.array([20.9, 27.2,31.4,27.3,30.0, 28.4, 29.7, 26.7, 27.1,26.8,27.1,25.3,25.3,26.4,27.5,27.4,25.3,25.0,30.3,30.2 ])

##LEBRON JAMES STATS
lebron_mean = lebron_ppg.mean()
lebron_meanY = np.array([-1,22])
lebron_meanX = np.array([lebron_mean, lebron_mean])
plt.plot(lebron_ppg,linewidth = 1, marker= 'o')
##lebron mean ppg
plt.plot(lebron_meanY,lebron_meanX, '#b8860b' )
#JORDAN STATS
jordan_ppg = np.array([23,22.9, 28.7,29.6,30.4,26.8,32.6,30.1,31.5,33.6,32.5,35,37.1,22.7,28.2 ])
jordan_mean = jordan_ppg.mean()
jordan_meanY = np.array([-1,22])
jordan_meanX = np.array([jordan_mean, jordan_mean])
plt.plot(jordan_ppg,linewidth = 1, marker= 'o')
##Jordan mean ppg
plt.plot(jordan_meanY,jordan_meanX, '#ff1a1a')
plt.show()
