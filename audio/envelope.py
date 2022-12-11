import time
import matplotlib.pyplot as plt
import numpy as np


class Envelope:
    # Classic ADSR envelope (A, S, R in ms, sustain as a proportion between 0 and 1)
    def __init__(self, sampling_rate=44100):
        self.sampling_rate = sampling_rate

    def generate_envelope(self, attack: float, decay: float, sustain: float, release: float, length=1.0):
        # generates numpy array of values between 0 and 1
        env_array = np.array([])
        attack_time_samples = int(attack / 1000 * self.sampling_rate)  # number of samples it takes for attack to happen
        decay_time_samples = int(decay / 1000 * self.sampling_rate)
        release_time_samples = int(release / 1000 * self.sampling_rate)
        sustain_time_samples = int(length * self.sampling_rate) - attack_time_samples - decay_time_samples - release_time_samples

        # Attack
        for i in range(attack_time_samples):
            env_array = np.append(env_array, i/attack_time_samples)

        # Decay
        magnitude = 1
        slope = (sustain - 1) / decay_time_samples
        for i in range(decay_time_samples):
            env_array = np.append(env_array, magnitude)
            magnitude += slope

        # Sustain
        for i in range(sustain_time_samples):
            env_array = np.append(env_array, sustain)

        # Release
        magnitude = sustain
        slope = -1 * sustain / release_time_samples
        for i in range(release_time_samples):
            env_array = np.append(env_array, magnitude)
            magnitude += slope

        return env_array

    def show_envelope_plot(self, env_array: np.array):
        plt.plot(env_array)
        plt.xlabel("Time")
        plt.ylabel("Amplitude")
        plt.show()
        return None


if __name__ == "__main__":
    env = Envelope()
    env.show_envelope_plot(env.generate_envelope(20, 50, 0.75, 200))
