from Encoder import Encoder
from Decoder import Decoder
import time
import os

error_counter = 0

for i in range(1,38):
    input_file = open(f"./tests/{i}/input.txt")
    text = input_file.read()
    input_file.close()

    start_time = time.time()

    encoder = Encoder(text)
    code = encoder.encoding()
    encoding_time = "%s секунд" % (time.time() - start_time)

    output_file = open(f"./tests/{i}/output.txt","w")
    output_file.write(str(float(code)))
    output_file.close()
    
    start_time = time.time()

    decoder = Decoder(code, encoder.n, encoder.m, encoder.alphabet, encoder.frequencies)
    result = decoder.decoding()
    decoding_time = "%s секунд" % (time.time() - start_time)

    res_file = open(f"./tests/{i}/result.txt", "w")
    res_file.write(f"Исходное сообщение: \n{text}\n")
    res_file.write(f"\nЗашифрованное сообщение: \n{str(float(code))}\n")
    res_file.write(f"\nРасшифрованное сообщение: \n{result}\n")
    
    if result == text:
        print(f"Тест {i} пройден")
        res_file.write(f"\nПрограмма правильно расшифровала код\n")

    else:
        error_counter += 1
        print(f"Тест {i} не пройден")
        res_file.write(f"Программа неправильно расшифровала код\n")

    coef = os.path.getsize(f"./tests/{i}/output.txt")/os.path.getsize(f"./tests/{i}/input.txt")

    res_file.close()

print("===========")
print(f"Было найдено {error_counter} ошибок")
        
        
        

    
