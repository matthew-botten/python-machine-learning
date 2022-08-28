from time import sleep
import sklearn
Import numpy
import matplotlib.pyplot as plt
randomNumbers = numpy.random.uniform(0.0, 5.0, 100000)
plt.hist(randomNumbers, 100)
plt.show()
