import os
import random
import glob
import numpy as np
import pickle
import pandas as pd
import json
from sklearn.metrics.pairwise import cosine_similarity

def random_choose(name):
    # random choose a antique song
    sample_id = random.randint(1,300)
    sample_name = name+'_'+str(sample_id).zfill(4)+'.npy'
    print(sample_name)
    return sample_name

if __name__ == '__main__':
    path='./avg_feature_arrays/'
    # original_name = json.loads('result.json')
    antique_sample_array = np.load(path+random_choose('antique'))
    antique_similarity = {}
    ballad_sample_array = np.load(path+random_choose('ballad'))
    ballad_similarity = {}
    jazz_sample_array = np.load(path+random_choose('jazz'))
    jazz_similarity = {}
    rap_sample_array = np.load(path+random_choose('rap'))
    rap_similarity = {}
    rock_sample_array = np.load(path+random_choose('rock'))
    rock_similarity = {}
    soft_sample_array = np.load(path+random_choose('soft'))
    soft_similarity = {}
    # calculate cosine_similarity
    files = os.listdir(path)
    for file in files:
        array = np.load(path+file)
        genre = file.split('_')[0]
        if genre=='antique':
            antique_similarity[cosine_similarity(antique_sample_array,array)[0].tolist()[0]]=file
        elif genre=='ballad':
            ballad_similarity[cosine_similarity(ballad_sample_array,array)[0].tolist()[0]]=file
        elif genre=='jazz':
            jazz_similarity[cosine_similarity(jazz_sample_array,array)[0].tolist()[0]]=file
        elif genre=='rap':
            rap_similarity[cosine_similarity(rap_sample_array,array)[0].tolist()[0]]=file
        elif genre=='rock':
            rock_similarity[cosine_similarity(rock_sample_array,array)[0].tolist()[0]]=file
        elif genre=='soft':
            soft_similarity[cosine_similarity(soft_sample_array,array)[0].tolist()[0]]=file

    antique_similarity=sorted(antique_similarity.items(), key=lambda d:d[0], reverse = True)
    ballad_similarity=sorted(ballad_similarity.items(), key=lambda d:d[0], reverse = True)
    jazz_similarity=sorted(jazz_similarity.items(), key=lambda d:d[0], reverse = True)
    rap_similarity=sorted(rap_similarity.items(), key=lambda d:d[0], reverse = True)
    rock_similarity=sorted(rock_similarity.items(), key=lambda d:d[0], reverse = True)
    soft_similarity=sorted(soft_similarity.items(), key=lambda d:d[0], reverse = True)

    # text = json.load('result.json')
    with open("./result.json",'r',encoding='UTF-8') as load_f:
        load_dict = json.load(load_f)
        # print(load_dict)
    with open("recomendation_result.txt","w",encoding='UTF-8') as f:
        file_name = antique_similarity[0][1].split('.')[0]
        f.write("古风测试歌曲：")
        f.write(load_dict["antique"][file_name+".mp3"]+"\n")
        for i in range(1,6):
            file_name = antique_similarity[i][1].split('.')[0]
            # print(load_dict["antique"][file_name+".mp3"])
            f.write("推荐歌曲"+str(i)+":")
            f.write(load_dict["antique"][file_name+".mp3"]+"\n")
        f.write("--------------------------------------------"+"\n")

        file_name = ballad_similarity[0][1].split('.')[0]
        f.write("民谣测试歌曲：")
        f.write(load_dict["ballad"][file_name+".mp3"]+"\n")
        for i in range(1,6):
            file_name = ballad_similarity[i][1].split('.')[0]
            # print(load_dict["ballad"][file_name+".mp3"])
            f.write("推荐歌曲"+str(i)+":")
            f.write(load_dict["ballad"][file_name+".mp3"]+"\n")
        f.write("--------------------------------------------"+"\n")

        file_name = jazz_similarity[0][1].split('.')[0]
        f.write("爵士测试歌曲：")
        f.write(load_dict["jazz"][file_name+".mp3"]+"\n")
        for i in range(1,6):
            file_name = jazz_similarity[i][1].split('.')[0]
            # print(load_dict["jazz"][file_name+".mp3"])
            f.write("推荐歌曲"+str(i)+":")
            f.write(load_dict["jazz"][file_name+".mp3"]+"\n")
        f.write("--------------------------------------------"+"\n")

        file_name = rap_similarity[0][1].split('.')[0]
        f.write("说唱测试歌曲：")
        f.write(load_dict["rap"][file_name+".mp3"]+"\n")
        for i in range(1,6):
            file_name = rap_similarity[i][1].split('.')[0]
            # print(load_dict["rap"][file_name+".mp3"])
            f.write("推荐歌曲"+str(i)+":")
            f.write(load_dict["rap"][file_name+".mp3"]+"\n")
        f.write("--------------------------------------------"+"\n")

        file_name = rock_similarity[0][1].split('.')[0]
        f.write("摇滚测试歌曲：")
        f.write(load_dict["rock"][file_name+".mp3"]+"\n")
        for i in range(1,6):
            file_name = rock_similarity[i][1].split('.')[0]
            # print(load_dict["rock"][file_name+".mp3"])
            f.write("推荐歌曲"+str(i)+":")
            f.write(load_dict["rock"][file_name+".mp3"]+"\n")
        f.write("--------------------------------------------"+"\n")

        file_name = soft_similarity[0][1].split('.')[0]
        f.write("轻音乐测试歌曲：")
        f.write(load_dict["soft"][file_name+".mp3"]+"\n")
        for i in range(1,6):
            file_name = soft_similarity[i][1].split('.')[0]
            # print(load_dict["soft"][file_name+".mp3"])
            f.write("推荐歌曲"+str(i)+":")
            f.write(load_dict["soft"][file_name+".mp3"]+"\n")
        f.write("--------------------------------------------"+"\n")
