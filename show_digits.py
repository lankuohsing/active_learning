# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 19:44:05 2020

@author: lankuohsing
"""

from sklearn.datasets import load_digits
digits = load_digits()
print(digits.data.shape)

import matplotlib.pyplot as plt
plt.gray()
plt.matshow(digits.images[0])
plt.show()
# In[]
"""样本和标签的获取"""
image_0=digits.images[0]
label_0=digits.target[0]