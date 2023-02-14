from Encoder import Encoder
from Decoder import Decoder
import time
import os


for i in range(1,101):
    input_file = open(f"./texts/{i}/input.txt")
    text = input_file.read()
    input_file.close()

    start_time = time.time()

    encoder = Encoder(text)
    code = encoder.encoding()
    encoding_time = "%s секунд" % (time.time() - start_time)

    output_file = open(f"./texts/{i}/output.txt","w+")
    output_file.write(str(float(code)))
    output_file.close()
    
    start_time = time.time()

    decoder = Decoder(code, encoder.n, encoder.m, encoder.alphabet, encoder.frequencies)
    result = decoder.decoding()
    decoding_time = "%s секунд" % (time.time() - start_time)

    print(f"Текст {i} сжат")
    
    res_file = open(f"./texts/{i}/result.txt", "w+")
    res_file.write(f"Время на кодирование: {encoding_time}\n")
    res_file.write(f"Время на декодирование: {decoding_time}\n")
    coef = os.path.getsize(f"./texts/{i}/output.txt")/os.path.getsize(f"./texts/{i}/input.txt")
    res_file.write(f"\nСтепень сжатия: {round(coef * 100, 2)}%")

    res_file.close()

        
        
        

    
