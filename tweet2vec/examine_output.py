import numpy as np
import scipy as sp
import scipy.stats

ha = np.load('./predictions_p.npy')
targets = np.load('./targets.pkl')
predictions = np.load('./predictions.npy')
data = np.load('./data.pkl')

ha.shape
ha[0].shape

sp.stats.describe(ha[0])

np.sum(ha[0],axis = 1)

np.sum(ha[0][0])
sp.stats.describe(ha[0][0])

sum(ha[0][0] > .5)


targets
predictions.shape
data


ha[0]
ha[1]


ha > 0.999