import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import tensorflow as tf


column_names = ["class", "sequence_name", "sequence"]
filepath = r'C:\Users\milam\OneDrive - ALS Bobi\Desktop\molecular+biology+splice+junction+gene+sequences\splice.data'
df = pd.read_csv(filepath, names=column_names, comment=';', header=None)

df = df[["class", "sequence"]]
max_length = df["sequence"].apply(len).max()
df["sequence"] = df["sequence"].apply(lambda seq: seq.ljust(max_length, "N"))

def encode_dna_sequences(sequences):
    base_map = {'A': [1, 0, 0, 0], 'C': [0, 1, 0, 0], 'G': [0, 0, 1, 0], 'T': [0, 0, 0, 1]}
    encoded = np.array([[base_map.get(base, [0, 0, 0, 0]) for base in seq] for seq in sequences])
    return encoded.reshape(len(encoded), -1)

X_real_encoded = encode_dna_sequences(df["sequence"])

label_map = {'N': 0, 'EI': 1, 'IE': 2}
y_real = df["class"].map(label_map).values

X_train, X_test, y_train, y_test = train_test_split(X_real_encoded, y_real, test_size=0.2, random_state=42)

input_size = X_train.shape[1]
hidden_size = 8
output_size = 3

model = tf.keras.Sequential([
    tf.keras.layers.Dense(hidden_size, input_shape=(input_size,), activation='tanh'),
    tf.keras.layers.Dense(output_size, activation='softmax')
])
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

model.fit(X_train, y_train, epochs=50, batch_size=32, validation_split=0.2)

test_loss, test_accuracy = model.evaluate(X_test, y_test)
train_loss, train_accuracy = model.evaluate(X_train, y_train)

print(f"Test Accuracy on DNA Data: {test_accuracy * 100:.2f}%")
print(f"Train Accuracy on DNA Data: {train_accuracy * 100:.2f}%")
