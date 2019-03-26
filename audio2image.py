import os

import threading  
import time  
class Convertor(threading.Thread): #The Convertor class is derived from the class threading.Thread  
    def __init__(self, num, interval, names):  
        threading.Thread.__init__(self)  
        self.thread_num = num  
        self.interval = interval  
        self.thread_stop = False
        self.names = names  
   
    def run(self): #Overwrite run() method, put what you want the thread do here  
        while not self.thread_stop:
            outputdir = "./image/"
            for name in self.names:
                count = 1
                path='./'+name+'/'
                files = os.listdir(path)
                for file in files:
                    print(file)
                    # strero=>mono
                    tmp_name = './'+name+'/'+'tmp.mp3'
                    input_file = './'+name+'/'+file
                    command = "sox "+input_file+" "+tmp_name+" remix 1,2"
                    os.system(command)
                    delete_file(input_file)
                    os.rename(tmp_name, input_file)
                    # get the spectrum
                    cmd = "sox "+'./'+name+'/'+file+" -n spectrogram -Y 300 -X 50 -m -r -o "+outputdir+name+'/'+os.path.splitext(file)[0]+'.png'
                    # os.rename(os.path.join(path,file),os.path.join(path,name+'_'+str(count).zfill(4)+os.path.splitext(file)[1]))
                    count = count + 1
                    os.system(cmd)
                    if count>=len(self.names)*len(files):
                        self.interval = True
            time.sleep(self.interval)  
    def stop(self):  
        self.thread_stop = True  
         
   
def test():
    names1 = ['antique','jazz']
    names2 = ['ballad','soft']
    names3 = ['rap','rock']

    thread1 = Convertor(1, 0.1, names1)  
    thread2 = Convertor(2, 0.1, names2)
    thread3 = Convertor(3, 0.1, names3)
    thread1.start()  
    thread2.start()
    thread3.start()
    return  

def delete_file(file_path):
    os.remove(file_path)

if __name__ == '__main__':
    test()