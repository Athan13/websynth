import matplotlib.pyplot as plt
import numpy as np
import math
import time


class Oscillator:
    def __init__(self, waveform: str, sampling_rate: float = 44100):
        self.sampling_rate = sampling_rate

        self.waveform = waveform
        assert self.waveform in ["sine", "triangle", "saw", "square"], \
            "Waveform must be sine, triangle, saw, or square."

    def generate_wave(self, duration: float = 1.0, freq: float = 440, amp: float = 1):
        wave_points = np.array([])

        if self.waveform == "sine":
            for i in range(int(self.sampling_rate * duration)):
                wave_points = np.append(wave_points, amp * np.sin(2 * np.pi * freq * i / self.sampling_rate))

        elif self.waveform == "square":
            for i in range(int(self.sampling_rate * duration)):
                p = i * freq / self.sampling_rate
                # p is how "far into" the period of the oscillation are you (one osc. = 1, halfway through = 0.5, etc)
                if p % 1 < 0.5:  # "decimal part" of p --> 9.5 % 1 = 0.5
                    wave_points = np.append(wave_points, amp)
                else:
                    wave_points = np.append(wave_points, -1 * amp)

        elif self.waveform == "saw":
            period = self.sampling_rate / freq
            for i in range(int(self.sampling_rate * duration)):
                wave_points = np.append(wave_points, 2 * (i / period - int(0.5 + i / period)))

        elif self.waveform == "triangle":
            period = self.sampling_rate / freq
            for i in range(int(self.sampling_rate * duration)):
                wave_points = np.append(wave_points, 4 * abs(i / period - math.floor(i / period + 0.5)) - 1)

        return wave_points

    def show_wave_plot(self, wave_points):
        plt.plot(wave_points)
        plt.xlabel("Time");
        plt.ylabel("Amplitude")
        plt.show()
        return None


if __name__ == "__main__":
    freq = 680.5432
    length = 5 / freq

    sine_osc = Oscillator("sine")
    plt.plot(sine_osc.generate_wave(length, freq, 1))

    saw_osc = Oscillator("saw")
    plt.plot(saw_osc.generate_wave(length, freq, 1))

    square_osc = Oscillator("square")
    plt.plot(square_osc.generate_wave(length, freq, 1))

    triangle_osc = Oscillator("triangle")
    plt.plot(triangle_osc.generate_wave(length, freq, 1))

    plt.xlabel("Time");
    plt.ylabel("Amplitude")
    plt.legend(["Sine", "Saw", "Square", "Triangle"])
    plt.show()
