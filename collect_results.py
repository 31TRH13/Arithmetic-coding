import matplotlib.pyplot as plt
import numpy as np

pathh = "./texts/"

"""
функция строит график зависимость времени кодирования к числу символов
"""
def draw_encoding_time():
    x = np.array([i[0] for i in data])
    y = np.array([float(i[1]) for i in data])

    plt.scatter(x, y)
    plt.xlabel("Length of input")
    plt.ylabel("Encoding time")
    plt.savefig("./static/encoding_time.png")
    

"""
функция строит график зависимость времени лекодирования к числу символов
"""
def draw_decoding_time():
    plt.clf()
    x = np.array([i[0] for i in data])
    y = np.array([float(i[2]) for i in data])

    plt.scatter(x, y, label="Decoding time", color='orange')
    plt.xlabel("Length of input")
    plt.ylabel("Decoding time")
    plt.savefig("./static/decoding_time.png")
    

"""
функция строит график зависимость степени сжатия к числу символов
"""
def draw_coef_graph():
    plt.clf()
    x = np.array([i[0] for i in data])
    y = np.array([float(i[3][:-1]) for i in data])
    y_max = max(y)
    y_min = min(y)
    step = (y_max - y_min) / 20
    plt.yticks(np.arange(y_min, y_max, step))   
    plt.scatter(x, y, color='green')
    plt.xlabel("Length of input")
    plt.ylabel("Compression coefficient")
    plt.savefig("./static/coef.png")


data = []
for i in range(1, 101):
    input = open(f"{pathh}{i}/input.txt")
    line = input.read()
    length = len(line)
    input.close()
    input = open(f"{pathh}{i}/result.txt")
    lines = input.read().split("\n")
    time_enc = lines[-4].split(" ")[-2]
    time_dec = lines[-3].split(" ")[-2]
    coef = lines[-1].split(" ")[-1]
    data.append([length, time_enc, time_dec, coef])


draw_encoding_time()
draw_decoding_time()
draw_coef_graph()



