# !gdown https://drive.google.com/uc?id=1qPlr30xLgt63l1yhPjf5R6l5RaENEO1w

# !pip install --upgrade --no-cache-dir gdown

# !gdown https://drive.google.com/uc?id=1mGt0ataFOa0qACVJTPsQ5GgoGQSLeOMx

# !unzip -qq casting_data.zip -d "/content/dataset"

# import pandas as pd
# import numpy as np
# import os
# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
# import time
# import matplotlib.pyplot as plt
# import cv2
# import seaborn as sns
# sns.set_style('darkgrid')
# import shutil
# from sklearn.metrics import confusion_matrix, classification_report
# from sklearn.model_selection import train_test_split
# import tensorflow as tf
# from tensorflow import keras
# from tensorflow.keras.preprocessing.image import ImageDataGenerator
# from tensorflow.keras.layers import Dense, Activation,Dropout,Conv2D, MaxPooling2D,BatchNormalization
# from tensorflow.keras.optimizers import Adam, Adamax
# from tensorflow.keras.metrics import categorical_crossentropy
# from tensorflow.keras import regularizers
# from tensorflow.keras.models import Model
# from tensorflow.keras import backend as K
# import time
# from tqdm import tqdm
# from sklearn.metrics import f1_score
# import sys
# if not sys.warnoptions:
#     import warnings
#     warnings.simplefilter("ignore")
# pd.set_option('display.max_columns', None)  # or 1000
# pd.set_option('display.max_rows', None)  # or 1000
# pd.set_option('display.max_colwidth', None)  # or 199
# print('Modules are loaded')

# def print_in_color(txt_msg,fore_tupple=(0,255,255),back_tupple=(100,100,100)):
#     #prints the text_msg in the foreground color specified by fore_tupple with the background specified by back_tupple 
#     #text_msg is the text, fore_tupple is foregroud color tupple (r,g,b), back_tupple is background tupple (r,g,b)
#     # default parameter print in cyan foreground and gray background
#     rf,gf,bf=fore_tupple
#     rb,gb,bb=back_tupple
#     msg='{0}' + txt_msg
#     mat='\33[38;2;' + str(rf) +';' + str(gf) + ';' + str(bf) + ';48;2;' + str(rb) + ';' +str(gb) + ';' + str(bb) +'m' 
#     print(msg .format(mat), flush=True)
#     print('\33[0m', flush=True) # returns default print color to back to black
#     return

# # example default print
# msg='test of default colors'
# print_in_color(msg)

# def make_dataframes(train_dir, test_dir):
#     dirlist=[train_dir,  test_dir]
#     names=['train', 'test']
#     zipdir=zip(names, dirlist)
#     for name,d in zipdir:
#         filepaths=[]
#         labels=[]
#         classlist=sorted(os.listdir(d) )       
#         for klass in classlist:
#             classpath=os.path.join(d, klass)           
#             flist=sorted(os.listdir(classpath)) 
#             desc=f'{name:6s}-{klass:25s}'
#             for f in tqdm(flist, ncols=130,desc=desc, unit='files', colour='blue'):
#                 fpath=os.path.join(classpath,f)
#                 filepaths.append(fpath)
#                 labels.append(klass)
#         Fseries=pd.Series(filepaths, name='filepaths')
#         Lseries=pd.Series(labels, name='labels')
#         df=pd.concat([Fseries, Lseries], axis=1) 
#         if name =='test':
#             test_df=df       
#         else:
#             pdf=df 
#     # split pdf into a train_df and a test_df
#     train_df, valid_df=train_test_split(pdf, train_size=.8, shuffle=True, random_state=123, stratify=pdf['labels'])
#     classes=sorted(train_df['labels'].unique())
#     class_count=len(classes)
#     sample_df=train_df.sample(n=50, replace=False)
#     # calculate the average image height and with
#     ht=0
#     wt=0
#     count=0
#     for i in range(len(sample_df)):
#         fpath=sample_df['filepaths'].iloc[i]
#         try:
#             img=cv2.imread(fpath)
#             h=img.shape[0]
#             w=img.shape[1]
#             wt +=w
#             ht +=h
#             count +=1
#         except:
#             pass
#     have=int(ht/count)
#     wave=int(wt/count)
#     aspect_ratio=have/wave
#     print('number of classes in processed dataset= ', class_count)    
#     counts=list(train_df['labels'].value_counts())    
#     print('the maximum files in any class in train_df is ', max(counts), '  the minimum files in any class in train_df is ', min(counts))
#     print('train_df length: ', len(train_df), '  test_df length: ', len(test_df), '  valid_df length: ', len(valid_df))  
#     print('average image height= ', have, '  average image width= ', wave, ' aspect ratio h/w= ', aspect_ratio)    
#     return train_df, test_df, valid_df, classes, class_count

# train_dir = r'/content/dataset/casting_data/train'
# test_dir=r'/content/dataset/casting_data/test'
# train_df, test_df, valid_df, classes, class_count=make_dataframes(train_dir, test_dir)

# def trim(df, max_samples, min_samples, column):
#     df=df.copy()
#     classes=df[column].unique()
#     class_count=len(classes)
#     length=len(df)
#     print ('dataframe initially is of length ',length, ' with ', class_count, ' classes')
#     groups=df.groupby(column)    
#     trimmed_df = pd.DataFrame(columns = df.columns)
#     groups=df.groupby(column)
#     for label in df[column].unique(): 
#         group=groups.get_group(label)
#         count=len(group)    
#         if count > max_samples:
#             sampled_group=group.sample(n=max_samples, random_state=123,axis=0)
#             trimmed_df=pd.concat([trimmed_df, sampled_group], axis=0)
#         else:
#             if count>=min_samples:
#                 sampled_group=group        
#                 trimmed_df=pd.concat([trimmed_df, sampled_group], axis=0)
#     print('after trimming, the maximum samples in any class is now ',max_samples, ' and the minimum samples in any class is ', min_samples)
#     classes=trimmed_df[column].unique()# return this in case some classes have less than min_samples
#     class_count=len(classes) # return this in case some classes have less than min_samples
#     length=len(trimmed_df)
#     print ('the trimmed dataframe now is of length ',length, ' with ', class_count, ' classes')
#     return trimmed_df, classes, class_count

# max_samples=500
# min_samples=500
# column='labels'
# train_df, classes, class_count=trim(train_df, max_samples, min_samples, column)

# def balance(df, n, working_dir, img_size):
#     df=df.copy()
#     print('Initial length of dataframe is ', len(df))
#     aug_dir=os.path.join(working_dir, 'aug')# directory to store augmented images
#     if os.path.isdir(aug_dir):# start with an empty directory
#         shutil.rmtree(aug_dir)
#     os.mkdir(aug_dir)        
#     for label in df['labels'].unique():    
#         dir_path=os.path.join(aug_dir,label)    
#         os.mkdir(dir_path) # make class directories within aug directory
#     # create and store the augmented images  
#     total=0
#     gen=ImageDataGenerator(horizontal_flip=True,  rotation_range=20, width_shift_range=.2,
#                                   height_shift_range=.2, zoom_range=.2)
#     groups=df.groupby('labels') # group by class
#     for label in df['labels'].unique():  # for every class               
#         group=groups.get_group(label)  # a dataframe holding only rows with the specified label 
#         sample_count=len(group)   # determine how many samples there are in this class  
#         if sample_count< n: # if the class has less than target number of images
#             aug_img_count=0
#             delta=n - sample_count  # number of augmented images to create
#             target_dir=os.path.join(aug_dir, label)  # define where to write the images
#             msg='{0:40s} for class {1:^30s} creating {2:^5s} augmented images'.format(' ', label, str(delta))
#             print(msg, '\r', end='') # prints over on the same line
#             aug_gen=gen.flow_from_dataframe( group,  x_col='filepaths', y_col=None, target_size=img_size,
#                                             class_mode=None, batch_size=1, shuffle=False, 
#                                             save_to_dir=target_dir, save_prefix='aug-', color_mode='rgb',
#                                             save_format='jpg')
#             while aug_img_count<delta:
#                 images=next(aug_gen)            
#                 aug_img_count += len(images)
#             total +=aug_img_count
#     print('Total Augmented images created= ', total)
#     # create aug_df and merge with train_df to create composite training set ndf
#     aug_fpaths=[]
#     aug_labels=[]
#     classlist=os.listdir(aug_dir)
#     for klass in classlist:
#         classpath=os.path.join(aug_dir, klass)     
#         flist=os.listdir(classpath)    
#         for f in flist:        
#             fpath=os.path.join(classpath,f)         
#             aug_fpaths.append(fpath)
#             aug_labels.append(klass)
#     Fseries=pd.Series(aug_fpaths, name='filepaths')
#     Lseries=pd.Series(aug_labels, name='labels')
#     aug_df=pd.concat([Fseries, Lseries], axis=1)         
#     df=pd.concat([df,aug_df], axis=0).reset_index(drop=True)
#     print('Length of augmented dataframe is now ', len(df))
#     return df 

# #n=200
# #working_dir=r'C:\Temp\coral'
# #img_size = (150,150)
# #train_df=balance(train_df, n, working_dir, img_size)

# working_dir=r'./'
# img_size = (200,200)# reduce image size to speed up training

# def make_gens(batch_size, train_df, test_df, valid_df, img_size):
#     trgen=ImageDataGenerator(horizontal_flip=True)    
#     t_and_v_gen=ImageDataGenerator()
#     msg='{0:70s} for train generator'.format(' ')
#     print(msg, '\r', end='') # prints over on the same line
#     train_gen=trgen.flow_from_dataframe(train_df, x_col='filepaths', y_col='labels', target_size=img_size,
#                                        class_mode='categorical', color_mode='rgb', shuffle=True, batch_size=batch_size)
#     msg='{0:70s} for valid generator'.format(' ')
#     print(msg, '\r', end='') # prints over on the same line
#     valid_gen=t_and_v_gen.flow_from_dataframe(valid_df, x_col='filepaths', y_col='labels', target_size=img_size,
#                                        class_mode='categorical', color_mode='rgb', shuffle=False, batch_size=batch_size)
#     # for the test_gen we want to calculate the batch size and test steps such that batch_size X test_steps= number of samples in test set
#     # this insures that we go through all the sample in the test set exactly once.
#     length=len(test_df)
#     test_batch_size=sorted([int(length/n) for n in range(1,length+1) if length % n ==0 and length/n<=80],reverse=True)[0]  
#     test_steps=int(length/test_batch_size)
#     msg='{0:70s} for test generator'.format(' ')
#     print(msg, '\r', end='') # prints over on the same line
#     test_gen=t_and_v_gen.flow_from_dataframe(test_df, x_col='filepaths', y_col='labels', target_size=img_size,
#                                        class_mode='categorical', color_mode='rgb', shuffle=False, batch_size=test_batch_size)
#     # from the generator we can get information we will need later
#     classes=list(train_gen.class_indices.keys())
#     class_indices=list(train_gen.class_indices.values())
#     class_count=len(classes)
#     labels=test_gen.labels
#     print ( 'test batch size: ' ,test_batch_size, '  test steps: ', test_steps, ' number of classes : ', class_count)
#     return train_gen, test_gen, valid_gen, test_batch_size, test_steps, classes


# batch_size=30
# train_gen, test_gen, valid_gen, test_batch_size, test_steps, classes=make_gens(batch_size, train_df, test_df, valid_df, img_size)

# def show_image_samples(gen ):
#     t_dict=gen.class_indices
#     classes=list(t_dict.keys())    
#     images,labels=next(gen) # get a sample batch from the generator 
#     plt.figure(figsize=(20, 25))
#     length=len(labels)
#     if length<25:   #show maximum of 25 images
#         r=length
#     else:
#         r=25
#     for i in range(r):        
#         plt.subplot(5, 5, i + 1)
#         image=images[i] /255       
#         plt.imshow(image)
#         index=np.argmax(labels[i])
#         class_name=classes[index]
#         plt.title(class_name, color='blue', fontsize=18)
#         plt.axis('off')
#     plt.show()
    
# show_image_samples(train_gen )

# def make_model(img_size, lr, mod_num=3):  
#     img_shape=(img_size[0], img_size[1], 3)
#     if mod_num == 0:
#         base_model=tf.keras.applications.efficientnet.EfficientNetB0(include_top=False, weights="imagenet",input_shape=img_shape, pooling='max')
#         msg='Created EfficientNet B0 model'
#     elif mod_num == 3:
#         base_model=tf.keras.applications.efficientnet.EfficientNetB3(include_top=False, weights="imagenet",input_shape=img_shape, pooling='max') 
#         msg='Created EfficientNet B3 model'
#     elif mod_num == 5:
#         base_model=tf.keras.applications.efficientnet.EfficientNetB5(include_top=False, weights="imagenet",input_shape=img_shape, pooling='max') 
#         msg='Created EfficientNet B5 model'
        
#     else:
#         base_model=tf.keras.applications.efficientnet.EfficientNetB7(include_top=False, weights="imagenet",input_shape=img_shape, pooling='max')
#         msg='Created EfficientNet B7 model'   
   
#     base_model.trainable=True
#     x=base_model.output
#     x=BatchNormalization(axis=-1, momentum=0.99, epsilon=0.001 )(x)
#     x = Dense(256, kernel_regularizer = regularizers.l2(l = 0.016),activity_regularizer=regularizers.l1(0.006),
#                     bias_regularizer=regularizers.l1(0.006) ,activation='relu')(x)
#     x=Dropout(rate=.4, seed=123)(x)       
#     output=Dense(class_count, activation='softmax')(x)
#     model=Model(inputs=base_model.input, outputs=output)
#     model.compile(Adamax(learning_rate=lr), loss='categorical_crossentropy', metrics=['accuracy']) 
#     msg=msg + f' with initial learning rate set to {lr}'
#     print_in_color(msg)
#     return model

# lr=.001
# model=make_model(img_size, lr) # using B3 model by default

# def make_model(img_size, lr, mod_num=3):  
#     img_shape=(img_size[0], img_size[1], 3)
#     if mod_num == 0:
#         base_model=tf.keras.applications.efficientnet.EfficientNetB0(include_top=False, weights="imagenet",input_shape=img_shape, pooling='max')
#         msg='Created EfficientNet B0 model'
#     elif mod_num == 3:
#         base_model=tf.keras.applications.efficientnet.EfficientNetB3(include_top=False, weights="imagenet",input_shape=img_shape, pooling='max') 
#         msg='Created EfficientNet B3 model'
#     elif mod_num == 5:
#         base_model=tf.keras.applications.efficientnet.EfficientNetB5(include_top=False, weights="imagenet",input_shape=img_shape, pooling='max') 
#         msg='Created EfficientNet B5 model'
        
#     else:
#         base_model=tf.keras.applications.efficientnet.EfficientNetB7(include_top=False, weights="imagenet",input_shape=img_shape, pooling='max')
#         msg='Created EfficientNet B7 model'   
   
#     base_model.trainable=True
#     x=base_model.output
#     x=BatchNormalization(axis=-1, momentum=0.99, epsilon=0.001 )(x)
#     x = Dense(256, kernel_regularizer = regularizers.l2(l = 0.016),activity_regularizer=regularizers.l1(0.006),
#                     bias_regularizer=regularizers.l1(0.006) ,activation='relu')(x)
#     x=Dropout(rate=.4, seed=123)(x)       
#     output=Dense(class_count, activation='softmax')(x)
#     model=Model(inputs=base_model.input, outputs=output)
#     model.compile(Adamax(learning_rate=lr), loss='categorical_crossentropy', metrics=['accuracy']) 
#     msg=msg + f' with initial learning rate set to {lr}'
#     print_in_color(msg)
#     return model

# lr=.001
# model=make_model(img_size, lr) # using B3 model by default

# class LR_ASK(keras.callbacks.Callback):
#     def __init__ (self, model, epochs,  ask_epoch, dwell=True, factor=.4): # initialization of the callback
#         super(LR_ASK, self).__init__()
#         self.model=model               
#         self.ask_epoch=ask_epoch
#         self.epochs=epochs
#         self.ask=True # if True query the user on a specified epoch
#         self.lowest_vloss=np.inf
#         self.lowest_aloss=np.inf
#         self.best_weights=self.model.get_weights() # set best weights to model's initial weights
#         self.best_epoch=1
#         self.plist=[]
#         self.alist=[]
#         self.dwell= dwell
#         self.factor=factor
        
#     def get_list(self): # define a function to return the list of % validation change
#         return self.plist, self.alist
#     def on_train_begin(self, logs=None): # this runs on the beginning of training
#         if self.ask_epoch == 0: 
#             print('you set ask_epoch = 0, ask_epoch will be set to 1', flush=True)
#             self.ask_epoch=1
#         if self.ask_epoch >= self.epochs: # you are running for epochs but ask_epoch>epochs
#             print('ask_epoch >= epochs, will train for ', epochs, ' epochs', flush=True)
#             self.ask=False # do not query the user
#         if self.epochs == 1:
#             self.ask=False # running only for 1 epoch so do not query user
#         else:
#             msg =f'Training will proceed until epoch {ask_epoch} then you will be asked to' 
#             print_in_color(msg )
#             msg='enter H to halt training or enter an integer for how many more epochs to run then be asked again'
#             print_in_color(msg)
#             if self.dwell:
#                 msg='learning rate will be automatically adjusted during training'
#                 print_in_color(msg, (0,255,0))
#         self.start_time= time.time() # set the time at which training started
       
#     def on_train_end(self, logs=None):   # runs at the end of training  
#         msg=f'loading model with weights from epoch {self.best_epoch}'
#         print_in_color(msg, (0,255,255))
#         model.set_weights(self.best_weights) # set the weights of the model to the best weights
#         tr_duration=time.time() - self.start_time   # determine how long the training cycle lasted         
#         hours = tr_duration // 3600
#         minutes = (tr_duration - (hours * 3600)) // 60
#         seconds = tr_duration - ((hours * 3600) + (minutes * 60))
#         msg = f'training elapsed time was {str(hours)} hours, {minutes:4.1f} minutes, {seconds:4.2f} seconds)'
#         print_in_color (msg) # print out training duration time
        
#     def on_epoch_end(self, epoch, logs=None):  # method runs on the end of each epoch
#         vloss=logs.get('val_loss')  # get the validation loss for this epoch
#         aloss=logs.get('loss')
#         if epoch >0:
#             deltav = self.lowest_vloss- vloss 
#             pimprov=(deltav/self.lowest_vloss) * 100 
#             self.plist.append(pimprov)
#             deltaa=self.lowest_aloss-aloss
#             aimprov=(deltaa/self.lowest_aloss) * 100
#             self.alist.append(aimprov)
#         else:
#             pimprov=0.0 
#             aimprov=0.0
#         if vloss< self.lowest_vloss:
#             self.lowest_vloss=vloss
#             self.best_weights=self.model.get_weights() # set best weights to model's initial weights
#             self.best_epoch=epoch + 1            
#             msg=f'\n validation loss of {vloss:7.4f} is {pimprov:7.4f} % below lowest loss, saving weights from epoch {str(epoch + 1):3s} as best weights'
#             print_in_color(msg, (0,255,0)) # green foreground
#         else: # validation loss increased
#             pimprov=abs(pimprov)
#             msg=f'\n validation loss of {vloss:7.4f} is {pimprov:7.4f} % above lowest loss of {self.lowest_vloss:7.4f} loading weights from epoch {str(self.best_epoch)} as model weights'
#             print_in_color(msg, (255,255,0)) # yellow foreground
#             if self.dwell: # if dwell is True when the validation loss increases the learning rate is automatically reduced and model weights are set to best weights
#                 lr=float(tf.keras.backend.get_value(self.model.optimizer.lr)) # get the current learning rate
#                 new_lr=lr * self.factor
#                 msg=f'learning rate was automatically adjusted from {lr:8.6f} to {new_lr:8.6f}, model weights set to best weights'
#                 print_in_color(msg) # cyan foreground
#                 tf.keras.backend.set_value(self.model.optimizer.lr, new_lr) # set the learning rate in the optimizer
#                 model.set_weights(self.best_weights) # set the weights of the model to the best weights      
                
#         if aloss< self.lowest_aloss:
#             self.lowest_aloss=aloss        
#         if self.ask: # are the conditions right to query the user?
#             if epoch + 1 ==self.ask_epoch: # is this epoch the one for quering the user?
#                 msg='\n Enter H to end training or  an integer for the number of additional epochs to run then ask again'
#                 print_in_color(msg) # cyan foreground
#                 ans=input()
                
#                 if ans == 'H' or ans =='h' or ans == '0': # quit training for these conditions
#                     msg=f'you entered {ans},  Training halted on epoch {epoch+1} due to user input\n'
#                     print_in_color(msg)
#                     self.model.stop_training = True # halt training
#                 else: # user wants to continue training
#                     self.ask_epoch += int(ans)
#                     if self.ask_epoch > self.epochs:
#                         print('\nYou specified maximum epochs of as ', self.epochs, ' cannot train for ', self.ask_epoch, flush =True)
#                     else:
#                         msg=f'you entered {ans} Training will continue to epoch {self.ask_epoch}'
#                         print_in_color(msg) # cyan foreground
#                         if self.dwell==False:
#                             lr=float(tf.keras.backend.get_value(self.model.optimizer.lr)) # get the current learning rate
#                             msg=f'current LR is  {lr:8.6f}  hit enter to keep  this LR or enter a new LR'
#                             print_in_color(msg) # cyan foreground
#                             ans=input(' ')
#                             if ans =='':
#                                 msg=f'keeping current LR of {lr:7.5f}'
#                                 print_in_color(msg) # cyan foreground
#                             else:
#                                 new_lr=float(ans)
#                                 tf.keras.backend.set_value(self.model.optimizer.lr, new_lr) # set the learning rate in the optimizer
#                                 msg=f' changing LR to {ans}'
#                                 print_in_color(msg) # cyan foreground

# epochs=40
# ask_epoch=10
# ask=LR_ASK(model, epochs,  ask_epoch)
# callbacks=[ask]

# history=model.fit(x=train_gen,  epochs=epochs, verbose=1, callbacks=callbacks,  validation_data=valid_gen,
#                validation_steps=None,  shuffle=False,  initial_epoch=0)
            
# import os
# model.save('/content/complete_defect_check.h5')

# import numpy as np
# import keras
# from keras.preprocessing import image

# # Load the pre-trained model
# # model = keras.models.load_model('complete_defect_check.h5')
# model = keras.models.load_model(model)

# # Load the input image
# img_path = '/content/dataset/casting_data/test/def_front/cast_def_0_1059.jpeg'
# img = image.load_img(img_path, target_size=(224,224))
# img_tensor = image.img_to_array(img)
# img_tensor = np.expand_dims(img_tensor, axis=0)
# img_tensor /= 255.

# # Get the prediction for the input image
# pred = model.predict(img_tensor)

# # Get the class with the highest probability
# pred_class = np.argmax(pred)

from tkinter import *

class Defect_Check:

    def __init__(self):
        pass
    
    def main(self):
        
        from tkinter import ALL
        import tkinter as tk
        from tkinter.font import Font
        from tkinter import filedialog as fd
        from tkinter import messagebox
        from PIL import Image, ImageTk
        import random
        import faulthandler
        faulthandler.enable()

        defect_check = Tk()
        defect_check.title('Defect Check')
        defect_check.geometry("800x800")
        defect_check.configure(bg = "#bed2fa")

        # Dimensions of window
        width = 1000
        height = 600

        # Sets the upper-left coordinate of the window
        defect_check.geometry("%dx%d+%d+%d" % (width, height, 220, 150))

        font_specifications_heading = Font(family = "Avenir Next", size = 36, underline = TRUE)
        font_specifications_regular = Font(family = "Avenir Next", size = 18)

        # Adding the heading of dashboard
        defect_check_page_header = Label(defect_check, text = "Defect Check", font = font_specifications_heading, fg = "black", bg = "#bed2fa")
        defect_check_page_header.place(x = 400, y = 50)

        def upload_image():
            global img
            # f_types = [('*.jpg')]
            filename = fd.askopenfilename()
            img = ImageTk.PhotoImage(file = filename)
            b2 =tk.Button(defect_check,image = img) # using Button 
            b2.place(x = 60, y = 200)


        def upload_image1():

            file_path = fd.askopenfilename()
            file_path = '/Users/nakulshah/Desktop/casting_512x512/def_front/cast_def_0_91.jpeg'
            
            if file_path:
                
                messagebox.showinfo("Success", "Image upladed succesfully!")

                # imageFrame = Frame(defect_check, bg="white")
                # imageFrame.place(x = 60, y = 200)

                # defectImage = PhotoImage(file = Image.open(file_path))
                # imageLabel = Label(defect_check, image = defectImage)
                # imageLabel.grid(row = 0, column = 0)

                # # Open the uploaded image using PIL
                # image = Image.open(file_path)
                # image = image.resize((256, 256))
                
                # # Convert the image to a PhotoImage object
                # image = ImageTk.PhotoImage(image)
                
                # # Display the image in a label
                # image_label = Label(defect_check, image = image)
                # image_label.place(x = 60, y = 200)
            
            else:
                messagebox.showerror("Error", "Failed to upload image")

            # Generate a random number that is either 0 or 1
            result = random.randint(0, 1)

            if result == 0:
                output_label = Label(defect_check, text = "Casting product is ready for supply", font = font_specifications_regular)
            else:
                output_label = Label(defect_check, text = "Casting product is defected :(", font = font_specifications_regular)
            
            output_label.place(x = 380, y = 450)

        # Upload an image
        upload_button = tk.Button(defect_check, text = "Upload Image", command = upload_image, font = font_specifications_regular)
        upload_button.place(x = 400, y = 150)

        def back_to_menu():
            from Menu import Menu
            defect_check.destroy()
            Menu().main()

        # Creating a back-to-menu button
        back_to_menu_button = Button(
            defect_check,
            text = "Back to Menu", 
            font = font_specifications_regular, 
            command = back_to_menu
        )
        
        back_to_menu_button.place(x = 820, y = 510)

        # Creating an exit button
        exit_button = Button(defect_check, text = "EXIT", font = font_specifications_regular, command = quit, width = 6)
        exit_button.place(x = 860, y = 15)

# Defect_Check().main()