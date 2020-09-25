import glob
import pandas as pd

# get data file names
path =r'C:\Users\62547\PycharmProjects\input files'# please change to your local path
filenames = glob.glob(path + "/*.csv")

dfs=[]
for filename in filenames:
   # data=pd.read_csv(filename)

    dfs.append( pd.read_csv(filename))

# Concatenate all data into one DataFrame
big_frame = pd.concat(dfs, axis=1, ignore_index=False)
big_frame.to_csv('out.csv')
