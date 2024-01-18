"""
TensorFlow 2 quickstart for beginners
"""

# https://www.tensorflow.org/tutorials/quickstart/beginner
import tensorflow as tf
from tensorflow.keras.optimizers.legacy import Adam
print("TensorFlow version:", tf.__version__)
print(f'GPU is: {tf.test.is_gpu_available()}')

mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10)
])

predictions = model(x_train[:1]).numpy()
predictions

tf.nn.softmax(predictions).numpy()

loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)

loss_fn(y_train[:1], predictions).numpy()

model.compile(optimizer=Adam(),
              loss=loss_fn,
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=2)

model.evaluate(x_test,  y_test, verbose=2)

probability_model = tf.keras.Sequential([
  model,
  tf.keras.layers.Softmax()
])

probability_model(x_test[:5])

print('Finish of test TensorFlow 2.0')
