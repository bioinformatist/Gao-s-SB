import pylab
import os
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

plt.style.use('ggplot')

print(os.getcwd())
depth_file_list = os.listdir("depth")
depth_table = pd.read_csv("depth" + os.sep + depth_file_list[0], sep = '\t', names=['Reference', 'Location', 'Depth'])
plt.figure()
ax = depth_table[['Location', 'Depth']].plot(kind = 'bar', x = 'Location', y = "Depth")
ax.set_xlim((0, 12000))
pylab.savefig('foo.png')
# print(depth_table)