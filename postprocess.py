import os
import pathlib
import torch 
import numpy as np 
import soundfile as sf


def get_files(data_location, extension):
    return list(pathlib.Path(data_location).rglob(f"*.{extension}"))

def peak_normalize(input_audio, db=-24.0):
    input_audio = torch.from_numpy(input_audio)
    input_audio /= input_audio.abs().max()
    input_audio *= 10 ** (db / 20)
    input_audio = input_audio.numpy()
    return input_audio

if __name__ == "__main__":
    data_location = 'assets/audios/2'
    save_location = 'assets/audios/b'
    files = get_files(data_location, 'wav')

    for f in files:
        f = str(f)
        f_name = f.split('/')[-1]
        print('> f name: ', f_name)

        wav, sr = sf.read(f)
        print('> wav length: ', len(wav))
        print('> sr: ', sr)

        wav = peak_normalize(wav)
        print(f'> max: {np.max(wav)} min: {np.min(wav)}')

        new_path = os.path.join(save_location, f_name)
        sf.write(new_path, wav, sr)
        