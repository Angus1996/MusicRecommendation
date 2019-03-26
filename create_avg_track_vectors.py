import os
import glob
import numpy as np
import pickle
import pandas as pd

vecs = glob.glob('feature_vec_arrays_single_file/*')
l = []
for v in vecs:
    print(v)
    v = v.split('\\')[1]
    file_name = v
    v = v.replace('.npy','')
    v = v.split('_')
    d = {
        'file_name':file_name,
        'genre':v[0],
        'song_id':v[0]+'_'+v[1],
        'spect_num':v[2]}
    l.append(d)
# l[0]
df = pd.DataFrame(l)
# df.sample(6)
song_genres = list(set(df['genre']))
song_ids = list(set(df['song_id']))
# for g in song_genres:
for s in song_ids:
    file_list = list(df[df['song_id'] == s]['file_name'])
    
    files = []
    for f in file_list:
        npy = np.load('feature_vec_arrays_single_file/{}'.format(f))
        files.append(npy)
    
    song_avg_vec = np.average(files, axis=0)
    save_name = 'avg_feature_arrays/{}.npy'.format(s)
    np.save(save_name, song_avg_vec)
