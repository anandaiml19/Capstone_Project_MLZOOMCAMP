# -*- coding: utf-8 -*-


import tensorflow as tf
from tensorflow.keras import models,layers
import matplotlib.pyplot as plt



"""# **Sizing and Scaling the Dataset**"""

resize_And_rescale=tf.keras.Sequential([
    layers.experimental.preprocessing.Resizing(255,255),
    layers.experimental.preprocessing.Rescaling(1./255)
])



"""## **Model Building**"""

input_shape = (32, 255, 255, 3)
n_classes = 5

model = models.Sequential([
    resize_And_rescale,
    layers.Conv2D(32, kernel_size = (3,3), activation='relu', input_shape=input_shape),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64,  kernel_size = (3,3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64,  kernel_size = (3,3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(n_classes, activation='softmax'),
])

model.build(input_shape=input_shape)

model.summary()

"""**Compiling the Model**"""

model.compile(
    optimizer='adam',
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=False),
    metrics=['accuracy']
)

outhistory = model.fit(
    train_ds,
    batch_size=32,
    validation_data=val_ds,
    verbose=1,
    epochs=30,
)

output_score=model.evaluate(test_ds)

model.save('model.h5')

"""## **Prediction with Model on Sample Image**"""

model=tf.keras.models.load_model('model.h5')

for img,label in test_ds.take(1):
  first_img=img[0].numpy().astype('uint8')
  first_label=label[0].numpy()
  print(img)
  print(label)
  pred_img=model.predict(img)
  plt.imshow(first_img)
  print("Actual label:", class_names[first_label])
  print("Predicted label:", class_names[np.argmax(pred_img[0])])

def predict(model,img):
  mangoimg_array=tf.keras.preprocessing.image.img_to_array(images[i].numpy())
  mangoimg_array=tf.expand_dims(mangoimg_array,0)

  predictions=model.predict(mangoimg_array)
  predicted_class=class_names[np.argmax(predictions[0])]
  out_confidence=round(100*np.max(predictions[0]),2)
  return predicted_class,out_confidence

plt.figure(figsize=(16,16))

for images,labels in test_ds.take(1):
  for i in range(9):
    ax=plt.subplot(3,3,i+1)
    plt.imshow(images[i].numpy().astype('uint8'))
    predicted_class,out_confidence=predict(model,images[i].numpy())

    actual_class=class_names[labels[i]]

    plt.title(f"Actual class: {actual_class},\nPredicted: {predicted_class},\nConfidence: {out_confidence}%")
    plt.axis('off')