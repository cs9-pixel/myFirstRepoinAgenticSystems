import numpy as np
import matplotlib.pyplot as plt

# 1. Epochs
epochs = np.arange(1, 11)

# 2. Synthetic loss values
np.random.seed(42)
loss = np.random.uniform(0.5, 1.0, size=10)

# 3. Line Plot (Loss vs Epoch)
plt.figure(figsize=(6, 4))
plt.plot(epochs, loss, marker='o')
plt.title("Loss vs Epoch")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.grid()
plt.show()

# 4. Scatter Plot (Epoch vs Loss)
plt.figure(figsize=(6, 4))
plt.scatter(epochs, loss)
plt.title("Epoch vs Loss")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.show()

# 5. Bar Chart (Model Accuracy)
models = ["Model A", "Model B", "Model C"]
accuracy = [0.85, 0.90, 0.88]

plt.figure(figsize=(6, 4))
plt.bar(models, accuracy)
plt.title("Model Accuracy Comparison")
plt.xlabel("Models")
plt.ylabel("Accuracy")
plt.show()
