import numpy as np
import scipy as sp
import scipy.stats

ha = np.load('./predictions_p.npy')
targets = np.load('./targets.pkl')
predictions = np.load('./predictions.npy')
data = np.load('./data.pkl')

ha.shape

np.sum(ha[0],axis = 1)

targets
predictions.shape
data

ha > 0.999