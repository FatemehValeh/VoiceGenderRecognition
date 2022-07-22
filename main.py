import os
import scipy.io.wavfile
import numpy as np
import math
from numpy import fft
import matplotlib.pyplot as plt
import sys


# --- question 2 ---
def spectrum(file_path):
    sampling_rate, data = scipy.io.wavfile.read(os.path.join(sys.path[0], "voices-wav", "voices", file_path))
    sum_of_data = data.sum(axis=1) / 2
    nyquist_rate = math.floor(len(sum_of_data) / 2)
    power = pow(abs(fft.fft(sum_of_data))[:nyquist_rate] / len(data) * 2, 2)
    frequency = fft.fftfreq(len(data), 1 / sampling_rate)[:nyquist_rate]
    return power, frequency


def draw_spectrum(power, frequency, title):
    plt.plot(frequency, power)
    plt.title(title)
    plt.xlim(xmin=15, xmax=1000)
    plt.xlabel("Frequency")
    plt.ylabel("Power")
    plt.show()


# --- question 3 ---
def max_freq(file_path):
    power, frequency = spectrum(file_path)
    return frequency[np.argmax(power)]


# --- question 4 ---
def gender(directory):
    result = []
    for file in os.listdir(directory):
        freq = max_freq(file)
        if freq < 180:
            result.append((file, "man"))
        else:
            result.append((file, "woman"))
    return result


def main():
    # woman_path = os.path.join(sys.path[0], "voices-wav\\voices\\v0.wav")
    # man_path = os.path.join(sys.path[0], "voices-wav\\voices\\v1.wav")
    # power, freq = spectrum(woman_path)
    # draw_spectrum(power, freq, "woman voice")
    # power, freq = spectrum(man_path)
    # draw_spectrum(power, freq, "man voice")
    # #
    # print("max frequency of v0.wav", max_freq(woman_path))
    # print("max frequency of v1.wav", max_freq(man_path))

    genders = gender(directory=os.path.join(sys.path[0], "voices-wav\\voices"))
    print(*genders, sep="\n")


if __name__ == '__main__':
    main()

