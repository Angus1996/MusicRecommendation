# 音乐推荐系统

2019-3-26日

参考网址：https://yq.aliyun.com/articles/154475
## 博客介绍
https://angus1996.github.io/post/keras%E3%80%81TensorFlow%E6%89%93%E9%80%A0%E9%9F%B3%E4%B9%90%E6%8E%A8%E4%BB%8B%E7%B3%BB%E7%BB%9F/

## 重要说明

除了sox命令转光谱因为要支持mp3格式，所以是在ubuntu16.04系统下操作，其余均是在windows10专业版下操作。

## 文件夹说明

**avg_feature_arrays** 是每一首歌曲的特征向量文件

**data** 是训练集、验证集、测试集的划分

**feature_vec_arrays_single_file** 是，每张256*256大小的图像的特征向量，通过平均同一首音乐的这些单独的特征向量，可以得到每一首歌的特征向量

**result** 是实验结果，分为四种参数组合：elu+adam，elu+rmsprop，relu+adam，relu+rmsprop，其中elu+adam效果最后，所以后续的推荐系统采用的是这种组合。子文件夹含有单独**ReadMe**说明文件，解释实验结果存图。

**参考代码** 是参考网址提供的代码，参考了其中一部分有价值的代码。

## 文件说明

**audio2image.py** ，将音频文件先做单声道转换处理，再做光谱图处理，得到每一首音乐的光谱图。

**cal_cosine_sim_make_recommendations.py**，随机在六种风格的音乐的300个特征向量中选择一个，与所有的1799个特征向量做余弦相似度比较，得到最高的六个特征向量（包括自己，余弦相似度为1），推荐五首歌曲，并由特征向量文件名反推原始数据歌曲名，输出到文本文件。

**create_avg_track_vector.py** ，将切割后的光谱图按照文件名进行加和求平均，得到每一首歌光谱图的特征向量

**create_feature_vectors.py**，调用模型得到切割后的每一个256*256大小的光谱图的特征向量

**getSlice.py**，切割每一首歌的整个的光谱图成若干256*256的小图

**model_test.py**，测试模型的表现，输出模型的分类报告和混淆矩阵

**model_train.py**，训练卷积神经网络的主程序

**music_classify.hdf5**，训练好的模型

**music_feature_extractor.hdf5**，可以提取特征的模型，提取的特征维度是128维，具体结构可以见下图。

**music_feature_extractor.py**，去掉训练好的模型的最后softmax层、最后的全连接层、最后的dropout层和一个激活层，得到可以提取特征的模型。

**recomendation_result.txt**，推荐结果输出文本

**rename.py**，重命名文件，读取原mp3数据，重命名为type_id的形式，如ballad_0001.mp3，并保存一一对应关系到**result.json** 文件中。

**result.json**，原始文件与重命名后的文件的一一对应关系

**sample.mp3、sample.png、sample.wav** 是测试sox命令的测试数据，包括mp3转wav，mp3转光谱。

