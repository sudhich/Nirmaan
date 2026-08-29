import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers


# Step 1: Load MNIST dataset
print("Loading MNIST dataset...")

(X_train, y_train), (X_test, y_test) = keras.datasets.mnist.load_data()


# Step 2: Display dataset information
print("Training images:", X_train.shape)
print("Training labels:", y_train.shape)
print("Testing images:", X_test.shape)
print("Testing labels:", y_test.shape)


# Step 3: Normalize pixel values
# Convert 0-255 into 0-1
X_train = X_train / 255.0
X_test = X_test / 255.0


# Step 4: Build the neural network
model = keras.Sequential([
    layers.Flatten(input_shape=(28, 28)),
    layers.Dense(128, activation="relu"),
    layers.Dense(10, activation="softmax")
])


# Step 5: Display model architecture
model.summary()


# Step 6: Compile the model
model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)


# Step 7: Train the model
print("\nTraining the model...")

history = model.fit(
    X_train,
    y_train,
    epochs=10,
    batch_size=32,
    validation_split=0.2
)


# Step 8: Evaluate the model
print("\nEvaluating the model...")

test_loss, test_accuracy = model.evaluate(
    X_test,
    y_test,
    verbose=0
)

print(f"Test Loss: {test_loss:.4f}")
print(f"Test Accuracy: {test_accuracy * 100:.2f}%")


# Step 9: Save the trained model
model.save("mnist_model.keras")

print("\nModel training completed!")
print("Model saved as: mnist_model.keras")