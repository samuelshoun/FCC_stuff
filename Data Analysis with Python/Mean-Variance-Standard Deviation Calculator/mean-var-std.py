'''
This is original code to complete the "Probability Calculator" challenge project at:
https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/mean-variance-standard-deviation-calculator

The full solution with unit tests are found at:
https://replit.com/@samuelshoun/boilerplate-mean-variance-standard-deviation-calculatorfork
'''

import numpy as np

def calculate(list):

    if len(list) != 9:
        raise ValueError('List must contain nine numbers.')

    arr = np.array(list)

    means = []
    varis = []
    sds = []
    maxes = []
    mins = []
    sums = []
    dct = {}

    for i in [(3,3), (9)]:
        arr = arr.reshape(i)
        for j in np.arange(arr.ndim):
            means.append(np.mean(arr, axis=j).tolist())
            varis.append(np.var(arr, axis=j).tolist())
            sds.append(np.std(arr, axis=j).tolist())
            maxes.append(np.max(arr, axis=j).tolist())
            mins.append(np.min(arr, axis=j).tolist())
            sums.append(np.sum(arr, axis=j).tolist())

    dct['mean'] = means
    dct['variance'] = varis
    dct['standard deviation'] = sds
    dct['max'] = maxes
    dct['min'] = mins
    dct['sum'] = sums

    return dct
