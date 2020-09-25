import glob
import pandas as pd

# get data file names
path =r'C:\Users\62547\PycharmProjects\input files'#please change to your own path
filenames = glob.glob(path + "/*.csv")
dfs=[pd.read_csv('s1 - Sheet1.csv', usecols=[0])]
for filename in filenames:
    data=pd.read_csv(filename, usecols=[1])
    dfs.append(data)
# Concatenate all data into one DataFrame
big_frame = pd.concat(dfs, axis=1, ignore_index=False)
big_frame.to_csv('out.csv')
