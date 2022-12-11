import matplotlib.pyplot as plt
import numpy as np
import math
import time

from oscillator import *
from envelope import *


class Note:
    def __init__(self, envelope: Envelope, oscillators: list, length: float, sampling_rate=44100):
        # Envelope is ADSR volume envelope; oscilators is list of oscillators;
        # length is length of note in seconds; sampling rate is in Hz
        self.envelope = envelope
        self.oscillators = oscillators
        self.length = length
        self.sampling_rate = sampling_rate

    def generate_note(self, volume=1):
        note_points = np.zeros(int(self.sampling_rate * self.length))

        # oscillators
        for osc in self.oscillators:
            osc_points = osc.generate_wave(length=self.length, sampling_rate=self.sampling_rate)
            note_points = note_points + osc_points

        # volume envelope
        volume_env = self.envelope.generate_envelope(length=self.length, sampling_rate=self.sampling_rate)
        note_points = note_points * volume_env

        # set volume final
        note_points = note_points / max(note_points) * volume

        return note_points

    def show_note_plot(self, note_array):
        plt.plot(note_array)
        plt.xlabel("Time")
        plt.ylabel("Amplitude")
        plt.show()
        return None

    def get_note_wav(self, note_array):
        pass
        # TODO: figure out array --> wav file

# TODO: filter
# TODO: stereo/pan effects
# TODO: effects (flanger, chorus, phaser)
# TODO: sine level


if __name__ == "__main__":
    env = Envelope(20, 50, 0.4, 100)

    osc1 = Oscillator(440, 0.7, "triangle")
    osc2 = Oscillator(440, 0.2, "saw")
    osc3 = Oscillator(220, 0.3, "sine")

    note = Note(env, [osc1, osc2, osc3], length=0.5)

    note.show_note_plot(note.generate_note())
