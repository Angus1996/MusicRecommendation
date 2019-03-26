import numpy as np
import os
from keras.models import load_model
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
from sklearn.metrics import confusion_matrix,classification_report
import matplotlib.pyplot as plt
from sklearn.utils.multiclass import unique_labels

def plot_confusion_matrix(confusion_matrix):
	plt.imshow(confusion_matrix, interpolation='nearest', cmap=plt.cm.Paired)
	plt.title("Confusion Matrix")
	plt.colorbar()
	tick_marks = np.arange(6)
	plt.xticks(tick_marks, tick_marks)
	plt.yticks(tick_marks, tick_marks)
	plt.ylabel("True Class")
	plt.xlabel("Predicted Class")
	plt.savefig("Confusion_matrix.jpg")
	plt.show()

def image_process(path,image):
	img = load_img(path+image)
	img_array = img_to_array(img)
	img_array = np.expand_dims(img_array, axis=0)
	img_array /= 255
	return img_array


def cal_acc(name, label):
	path='./data/test/'+name+'/'
	files = os.listdir(path)
	total_count = len(files)
	print(name+" count:", total_count)
	y_pred_true=0
	for file in files:
		# print(file)
		prediction=model.predict(image_process(path,file))
		prediction=prediction.tolist()
		if prediction[0].index(max(prediction[0]))==int(label):
			y_pred_true=y_pred_true+1
	acc = y_pred_true*1.0/total_count
	print("yuce: ", y_pred_true)
	return acc

if __name__ == '__main__':
	model = load_model('./model.h5')

	names = ['antique','ballad','jazz','rap','rock','soft']
	pre = model.predict(image_process('./data/test/rock/', 'rock_0272_000.png'))
	print(pre)
	# for name in names:
	# 	print(name+" acc:", cal_acc(name, names.index(name)))

	y_pred=[]
	y_true=[]
	for name in names:
		count = 1
		path='./data/test/'+name+'/'
		files = os.listdir(path)
		for file in files:
			print(file)
			if name=='antique':
				y_true.append(0)
			elif name=='ballad':
				y_true.append(1)
			elif name=='jazz':
				y_true.append(2)
			elif name=='rap':
				y_true.append(3)
			elif name=='rock':
				y_true.append(4)
			elif name=="soft":
				y_true.append(5)
			count = count + 1
			prediction=model.predict(image_process(path,file))
			prediction=prediction[0].tolist() 
			# print(prediction.index(max(prediction)))
			y_pred.append(prediction.index(max(prediction)))

	confusion_mat = confusion_matrix(y_true, y_pred)
	plot_confusion_matrix(confusion_mat)

	target_names = names
	print(classification_report(y_true, y_pred, target_names=target_names))