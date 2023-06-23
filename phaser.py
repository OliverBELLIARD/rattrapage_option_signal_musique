import numpy as np
import scipy.io.wavfile as wavfile

# Parameters
# **********

# This must be an audio file readable by scipy.io.wavfile.read() function
# A converted version of the original 'Clean Electric Guitar Loop.mp3' file is provided in this project
input_file = 'Clean-Electric-Guitar-Loop.wav'
output_file = 'output.wav'

# Effect parameters
d = 100  # Intensity of the effect
f = 3    # Speed of the effect
depth_control = 0.7 # Depth control factor

# Read input file
# ***************

fs, input_data = wavfile.read(input_file, mmap=True)
# convert to float
max_value = float(-np.iinfo(input_data.dtype).min)
input_data = input_data.astype('float32') / max_value
# convert to mono if not already
if len(input_data.shape) > 1:
    input_data = np.mean(input_data, axis=1)
input_data = input_data.flatten()


# Audio data process
# ******************

output_data = np.zeros(len(input_data))

# Phase shifting effect processing
for n in range(d-1):
  output_data[n] = input_data[n]

for n in range(d,len(input_data)):
  phase_shift_samples = int((np.sin(f*2*np.pi*n/fs)+1)*d/2)
  output_data[n] = (input_data[n]*depth_control
                    -input_data[n-phase_shift_samples])/2

# Testing: all pass, noprocessing
# output_data = input_data
# *************************

# Save output
# ***********
output_data = 0.99 * output_data / max(abs(output_data))
wavfile.write(output_file, int(fs), (output_data*np.iinfo(np.int16).max).astype(np.int16))