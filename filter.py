import time
import matplotlib.pyplot as plt
import numpy as np
from scipy.fft import fft, ifft


class Filter:
    def __init__(self, type: str):
        self.type = type
        assert self.type in ["LPF", "HPF", "BPF", "BSF"], "Filter type must be LPF, HPF, BPF, BSF"

    def generate_filter(self, *cutoffs, resonance: float, note_num_samples=44100):
        """"
        Generates filter in the style of Envelope.generate_envelope(): returns a numpy array of coefficients between 0
        and 1 that are then multiplied with FFT of the sound in Filter.filter_freqs()
        """

        if len(tuple) == 1 and self.type in ["LPF", "HPF"]:
            cutoff = cutoffs[0]
        elif len(tuple) == 2 and self.type in ["BPF", "BSF"]:
            cutoff_low, cutoff_high = cutoffs
            assert cutoff_low < cutoff_high, "Low cutoff must be lower than high cutoff"
        else:
            raise Exception("LPFs, HPFs must have one cutoff; BPFs, BSFs must have two cutoffs")

        assert 0 < resonance < 1, "Resonance must be between 0 and 1"

        filter_coeffs = np.array(note_num_samples)

        if self.type == "LPF":
            pass
        elif self.type == "HPF":
            pass
        elif self.type == "BPF":
            pass
        elif self.type == "BSF":
            pass

        return filter_coeffs

    def filter_freqs(self, note):
        # Does all the FFT stuff and filters out the freqs we don't want, returns new "note" array
        pass


if __name__ == "__main__":
    lpf = Filter("LPF")
