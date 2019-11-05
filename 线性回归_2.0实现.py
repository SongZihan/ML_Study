import tensorflow as tf
from tensorflow.keras import layers
import numpy as np
import matplotlib.pyplot as plt
# 使用numpy生成200个随机点
x_data = np.linspace(-0.5,0.5,1000)[:,np.newaxis] # 加一个轴

noise = np.random.normal(0,0.01,x_data.shape)
# np.set_printoptions(suppress=True)
y_data = np.square(x_data)+noise
# plt.figure()
# plt.scatter(x_data,y_data)
#
# plt.show()




model = tf.keras.Sequential()
model.add(layers.Dense(10,input_shape = (1,),activation = "tanh"))
model.add(layers.Dense(1,activation = "tanh"))
model.compile(loss=tf.keras.losses.mse
              ,optimizer=tf.keras.optimizers.Adam(0.001))
model.fit(x_data,y_data,epochs=2000)
k = model.predict(x_data)

plt.figure()
plt.scatter(x_data,y_data)
plt.plot(x_data,k,"r-")
plt.show()







