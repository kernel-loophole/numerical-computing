import numpy as np
import numpy.ma as ma
x = np.array([1, 2, 3])
x.view(ma.MaskedArray)
x = [0.,1.,-9999.,3.,4.]
mx = ma.masked_values (x, -9999.)
print(mx)
