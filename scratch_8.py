import glob
import pandas as pd

# get data file names
path =r'C:\Users\62547\PycharmProjects\input files'
filenames = glob.glob(path + "/*.csv")

dfs=[]
for filename in filenames:
   # data=pd.read_csv(filename)

    dfs.append( pd.read_csv(filename))

# Concatenate all data into one DataFrame
big_frame = pd.concat(dfs, axis=1, ignore_index=False)
#big_frame = pd.DataFrame(columns=['','time','s1', 's2', 's3','s4','s5','s6','s7','s8','s9','s10'])
big_frame.to_csv('out.csv')
