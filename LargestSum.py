import numpy as np
List8 = np.array([[0,9,8,7], [0,0,9,8], [4,5,6,7]])
rowsum = np.sum(List8, axis=1)
print('row {} has the maximum sum with a sum value of {}'.format(np.argmax(rowsum)+1, np.max(rowsum)))