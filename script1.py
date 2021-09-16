from scipy.io.wavfile import write
from scipy.io import wavfile
import matplotlib.pyplot as plt
import numpy as np

samplerate, data_st = wavfile.read('WAV/Start_of_transmission.wav')
samplerate, data_en = wavfile.read('WAV/End_of_transmission.wav')
samplerate, data_00 = wavfile.read('WAV/0.wav')
samplerate, data_01 = wavfile.read('WAV/1.wav')
samplerate, data_02 = wavfile.read('WAV/2.wav')
samplerate, data_03 = wavfile.read('WAV/3.wav')
samplerate, data_04 = wavfile.read('WAV/4.wav')
samplerate, data_05 = wavfile.read('WAV/5.wav')
samplerate, data_06 = wavfile.read('WAV/6.wav')
samplerate, data_07 = wavfile.read('WAV/7.wav')
samplerate, data_08 = wavfile.read('WAV/8.wav')
samplerate, data_09 = wavfile.read('WAV/9.wav')
samplerate, data_10 = wavfile.read('WAV/10.wav')
samplerate, data_11 = wavfile.read('WAV/11.wav')
samplerate, data_12 = wavfile.read('WAV/12.wav')
samplerate, data_13 = wavfile.read('WAV/13.wav')
samplerate, data_14 = wavfile.read('WAV/14.wav')
samplerate, data_15 = wavfile.read('WAV/15.wav')
samplerate, data_16 = wavfile.read('WAV/16.wav')
samplerate, data_17 = wavfile.read('WAV/17.wav')
samplerate, data_18 = wavfile.read('WAV/18.wav')
samplerate, data_19 = wavfile.read('WAV/19.wav')
samplerate, data_20 = wavfile.read('WAV/20.wav')
samplerate, data_21 = wavfile.read('WAV/21.wav')
samplerate, data_22 = wavfile.read('WAV/22.wav')
samplerate, data_23 = wavfile.read('WAV/23.wav')
samplerate, data_24 = wavfile.read('WAV/24.wav')
samplerate, data_25 = wavfile.read('WAV/25.wav')

data = [data_00, data_01, data_02, data_03, data_04, data_05, data_06, data_07, data_08, data_09,
        data_10, data_11, data_12, data_13, data_14, data_15, data_16, data_17, data_18, data_19,
        data_20, data_21, data_22, data_23, data_24, data_25]

symbols = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z'];
file_path = "C:/users/ulgeo/OneDrive/Desktop/keys.txt"

def vigener_f(a, b):
    return (a + b) % 26;

def vigener_de_f(c, b):
    if c - b >= 0:
        return c - b;
    else:
        return c - b + 26;

def a1z26(value):
    if(len(value) == 1):
        return symbols.index(value)
    else:
            result = "";
            for ch in value:
                    result += str(a1z26(ch)) + " ";
            return result;

def de_a1z26(value):
    return symbols[int(value)];

def encrypt(_message, _key):
    message = _message.upper();
    key = _key.upper();

    if len(key) > len(message):
        key = _key[:len(_message)];
    elif len(key) < len(message):
        len_m = len(_message);
        len_k = len(_key);
        key = ""
        while (len_m > len_k):
            key += _key;
            len_m -= len_k;
        key += _key[:len_m];

    result = "";
    for i in range(len(message)):
        result += de_a1z26(vigener_f(a1z26(message[i]), a1z26(key[i])));
    return result;

def decrypt(_message, _key):
    message = _message.upper();
    key = _key.upper();
    if len(key) > len(message):
        key = _key[:len(_message)];
    elif len(key) < len(message):
        len_m = len(_message);
        len_k = len(_key);
        key = ""
        while (len_m > len_k):
            key += _key;
            len_m -= len_k;
        key += _key[:len_m];

    result = "";
    for i in range(len(message)):
        result += de_a1z26(vigener_de_f(a1z26(message[i]), a1z26(key[i])));
    return result;

def de_inp(input_str):
    inp = input_str.split()
    return inp

def ret_file_dat(value):
    x = int(value)
    return data[x]

def create_file(inp):
    data_new = data_st.copy()
    for x in inp:
        data_new = np.concatenate((data_new, ret_file_dat(x)))
    data_new = np.concatenate((data_new, data_en))

    length = data_new.shape[0] / samplerate
    print(f"length = {length}s")
    time = np.linspace(0., length, data_new.shape[0])
    # plt.plot(time, data_new[:, 0], label="Left channel")
    # plt.plot(time, data_new[:, 1], label="Right channel")
    # plt.legend()
    # plt.xlabel("Time [s]")
    # plt.ylabel("Amplitude")
    # plt.show()

    write("example.wav", samplerate, data_new.astype(np.int16))

print('Cript/decrypt?\nType c or d')
k = input();
if k == 'c':
    print('Type message:')
    message = input()
    print('Type key:')
    key = input()
    inpu = a1z26(encrypt(message, key))
    print(inpu);
    create_file(de_inp(inpu))
    input();
elif k == 'd':
    print('Type message:')
    crypto = input();
    print('Type key:')
    key = input();
    mas = de_inp(crypto)
    cry_mesg = ''
    for x in mas:
        cry_mesg += de_a1z26(x);
    outpu = decrypt(cry_mesg, key);
    print(outpu);
    input();
