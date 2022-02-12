import tensorflow as tf
import numpy as np

model = tf.keras.models.load_model('../models/mymodel.h5')

image = np.random.rand(224, 224, 3)
print(image.shape)

data = np.array([image])
print(data.shape)

predict = model.predict(data)
print(predict)

print(np.argmax(predict))