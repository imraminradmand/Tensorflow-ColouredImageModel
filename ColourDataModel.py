#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


import tensorflow as tf
from tensorflow.keras.datasets import cifar10


# In[4]:


(x_train, y_train), (x_test, y_test) = cifar10.load_data()


# In[5]:


x_train[0].shape


# no need to reshape, got what i need

# In[6]:


x_train = x_train /255


# In[7]:


x_test = x_test/255


# In[8]:


y_test


# In[10]:


from tensorflow.keras.utils import to_categorical


# In[11]:


y_cat_train = to_categorical(y_train, 10)


# In[12]:


y_cat_test = to_categorical(y_test, 10)


# need to change the values to categories

# In[13]:


plt.imshow(x_train[0])


# In[14]:


from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Conv2D, MaxPool2D, Flatten


# In[15]:


model = Sequential()

model.add(Conv2D(filters=32, kernel_size=(4,4), input_shape=(32,32,3), activation='relu')) #grab input shape from the code we ran earlier
model.add(MaxPool2D(pool_size=(2, 2)))

model.add(Conv2D(filters=64, kernel_size=(4,4), input_shape=(32,32,3), activation='relu')) #grab input shape from the code we ran earlier
model.add(MaxPool2D(pool_size=(2, 2)))

model.add(Flatten())

model.add(Dense(256, activation = 'relu')) #more complex since colours are involved so added more neurons

model.add(Dense(10, activation='softmax')) #softmax since multiclass problem

model.compile(loss='categorical_crossentropy', optimizer = 'adam', metrics = ['accuracy'])


# In[16]:


from tensorflow.keras.callbacks import EarlyStopping


# In[17]:


early_stop = EarlyStopping(monitor='val_losses', patience = 3)


# In[18]:


model.fit(x_train, y_cat_train, epochs=20, 
         validation_data = (x_test, y_cat_test), callbacks=[early_stop])


# 96% accuracy on last round

# In[19]:


metrics = pd.DataFrame(model.history.history)


# In[20]:


metrics[['accuracy', 'val_accuracy']].plot()


# In[21]:


metrics[['loss', 'val_loss']].plot()


# stop training at like 7 epochs cause it aint looking good

# In[22]:


from sklearn.metrics import classification_report, confusion_matrix


# In[23]:


predictions = model.predict_classes(x_test)


# In[24]:


print(classification_report(y_test, predictions))


# Considering model would have a 1/10 chance of being right, we got some good accuracy

# doesnt do too good with cats and dog

# Does good with cars considering there is a trucks category too

# In[25]:


print(confusion_matrix(y_test, predictions))


# In[27]:


import seaborn as sns

plt.figure(figsize=(10,7))
sns.heatmap(confusion_matrix(y_test, predictions), annot=True)


# some confusion between 3 and 5 

# In[26]:


test = x_test[6]


# In[30]:


plt.imshow(test.reshape(32,32,3))


# In[32]:


model.predict_classes(test.reshape(1,32,32,3))


# In[33]:


from tensorflow.keras.models import load_model


# In[34]:


model.save('colourimagepredictor.h5')


# In[ ]:




