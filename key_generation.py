import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
import tkinter as tk
from tkinter import messagebox

# Generate chaotic data using a logistic map
def generate_chaotic_data(n=1000, seed=0.5, r=3.99):
    x = seed
    chaotic_series = []
    for _ in range(n):
        x = r * x * (1 - x)  # Logistic map equation
        chaotic_series.append(x)
    return np.array(chaotic_series)

# Prepare dataset
data = generate_chaotic_data(1000).reshape(-1, 1)
X_train, y_train = data[:-1], data[1:]  # Sequential learning

# Define LSTM model
model = Sequential([
    LSTM(64, return_sequences=True, input_shape=(1, 1)),
    LSTM(32, return_sequences=False),
    Dense(10, activation='sigmoid')  # Output 10 ASCII characters
])

# Compile & train model
model.compile(optimizer='adam', loss='mse')
model.fit(X_train.reshape(-1, 1, 1), y_train, epochs=50, batch_size=32)

# Function to generate a random 80-bit (10-character) key
def generate_key():
    chaotic_input = np.array([[np.random.rand()]]).reshape(1, 1, 1)
    key_values = model.predict(chaotic_input).flatten()

    # Convert values to ASCII characters
    generated_key = ''.join([chr(int(b * 94) + 33) for b in key_values])  
    return generated_key
