import os

import matplotlib.pyplot as plt
import pandas as pd

plt.style.use('ggplot')

tdir = "depth_16"
depth_file_list = os.listdir(tdir)
depth_file_list_len = len(depth_file_list)

plt.figure(figsize=(8, 35))
for i, depth_file in enumerate(depth_file_list):
    df = pd.read_table(tdir + os.sep + depth_file, names=['Reference', 'Location', 'Depth'], sep='\t')
    plt.subplot(depth_file_list_len, 1, i + 1)
    plt.bar(df['Location'], df['Depth'])
    plt.title(depth_file)

plt.tight_layout()
plt.savefig("16.png")
plt.close()
