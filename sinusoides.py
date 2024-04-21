import numpy as np
import matplotlib.pyplot as plt

# Time array
t = np.linspace(0, 2*np.pi, 1000)

# Sinusoidal waves
frequencies = [1, 2, 3]  # Frequencies of the sinusoidal waves
amplitudes = [1, 0.5, 0.3]  # Amplitudes of the sinusoidal waves

sinusoids = []
for freq, amp in zip(frequencies, amplitudes):
    sinusoids.append(amp * np.sin(2*np.pi*freq*t))

# Plot individual sinusoids
plt.figure(figsize=(10, 6))
for i, sin in enumerate(sinusoids):
    plt.plot(t, sin, label=f"Sinusoid {i+1}")

plt.title("Individual Sinusoidal Waves")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.show()

# Sum of sinusoidal waves
sum_wave = np.sum(sinusoids, axis=0)

# Plot the sum
plt.figure(figsize=(10, 6))
plt.plot(t, sum_wave, color='red', label="Sum of Sinusoids")
plt.title("Sum of Sinusoidal Waves")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.show()
