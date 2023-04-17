import os
import pathlib
import torch 
import numpy as np 
import soundfile as sf
import cv2

def get_files(data_location, extension):
    return list(pathlib.Path(data_location).rglob(f"*.{extension}"))

def peak_normalize(input_audio, db=-24.0):
    input_audio = torch.from_numpy(input_audio)
    input_audio /= input_audio.abs().max()
    input_audio *= 10 ** (db / 20)
    input_audio = input_audio.numpy()
    return input_audio

if __name__ == "__main__":
    x_size = 400
    y_size = 300

    img = cv2.imread('/Users/yeh/Desktop/ptpty.github.io/assets/case_0/bias_variation_0.png')
    size = (img.shape[1], img.shape[0])
    
    ime = cv2.resize(img, (x_size, y_size), interpolation=cv2.INTER_AREA)

    cv2.imwrite('/Users/yeh/Desktop/ptpty.github.io/assets/case_0/bias_variation_0_change.png', img)

    img = cv2.imread('/Users/yeh/Desktop/ptpty.github.io/assets/case_1/signal_spec.png')
    size = (img.shape[1], img.shape[0])
    
    ime = cv2.resize(img, (x_size, y_size), interpolation=cv2.INTER_AREA)

    cv2.imwrite('/Users/yeh/Desktop/ptpty.github.io/assets/case_1/signal_spec_change.png', img)