import numpy as np
import sounddevice as sd
import random
import time
import math

def generate_noise(duration, sample_rate=44100, mean=0, std=0.5, vol=2.0):
    """
    Generate audio noise.

    Parameters:
        duration (float): Duration of the audio in seconds.
        sample_rate (int): Sampling rate of the audio (default is 44100 Hz).
        mean (float): Mean of the normal distribution (default is 0).
        std (float): Standard deviation of the normal distribution (default is 0.5).

    Returns:
        numpy.ndarray: Array of audio samples representing the generated noise.
    """
    # Calculate the number of samples based on duration and sample rate
    num_samples = int(duration * sample_rate)

    # Generate more random noise
    noise = np.random.normal(mean, std, num_samples)

    # Increase the amplitude to make the noise louder
    noise *= vol

    return noise

def play_audio(samples, sample_rate=44100):
    """
    Play audio.

    Parameters:
        samples (numpy.ndarray): Array of audio samples.
        sample_rate (int): Sampling rate of the audio (default is 44100 Hz).
    """
    sd.play(samples, sample_rate)
    sd.wait()

if __name__ == "__main__":
    while True:
        fd = open('log_of_apm.txt', 'r')
        #print(fd.readlines()[-1])
        apm = int(fd.readlines()[-1].split(':')[-1].strip())
        fd.close()

        a, b = 0.4, 0.8
        # target apm will be midpoint between min and max
        minapm = 60
        maxapm = 180

        if apm <= minapm:
            vol = 2.0
        elif apm >= maxapm:
            vol = 2.0
        else:
            # apm in 60-120
            r = (apm - minapm) / (maxapm - minapm)
            # r from 0 to 1
            r = abs(r - 0.5)
            # r distance to 0.5
            vol = r * 2.0
        print("APM:", apm, "vol", vol)

        noise_duration = random.uniform(a, b)
        noise = generate_noise(noise_duration, vol=vol)
        play_audio(noise)

        sleep_duration = random.uniform(a, b)
        #time.sleep(sleep_duration)
