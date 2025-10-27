import os
import tensorflow as tf 
from tensorflow.keras import layers, models 
import pickle

train_dir = "data/train"
val_dir = "data/validation"

batch_size = 32
img_height = img_width = 128

train_ds = tf.keras.preprocessing.image_dataset_from_directory(
        train_dir,
        labels="inferred",
        label_mode="binary",
        image_size=(img_height, img_width),
        batch_size=batch_size,
)

val_ds = tf.keras.preprocessing.image_dataset_from_directory(
        val_dir,
        labels="inferred",
        label_mode="binary",
        image_size=(img_height, img_width),
        batch_size=batch_size,
)

base_model = tf.keras.applications.MobileNetV2(
        input_shape=(img_height, img_width, 3),
        include_top = False,
        weights="imagenet",
)

base_model.trainable = False

model = models.Sequential([
    base_model,
    layers.GlobalAveragePooling2D(),
    layers.Dropout(0.3),
    layers.Dense(1, activation="sigmoid")
])

model.compile(
    optimizer=tf.keras.optimizers.Adam(1e-4),
    loss="binary_crossentropy",
    metrics=["accuracy"],
)

model.fit(train_ds, validation_data=val_ds, epochs=8)

model.save('public/key_model/key_classifier_full.h5', save_format='h5')

# pickle.dump(model, open("public/key_model/model.pkl", "wb"))
