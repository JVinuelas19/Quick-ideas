import time
import random 
import os

#Generates a random line
def gen_random_sequence(prob, previous_line, change):
    sequence = list()
    for i in range(234):
        if change:
            if random.random()<prob:
                sequence.append(chr(random.randint(33,126)))
            else:
                sequence.append(" ")
        else:
            if previous_line[i] != " ":
                sequence.append(chr(random.randint(33,126)))
            else:
                if random.random()<prob:

                    sequence.append(chr(random.randint(33,126)))
                else:
                    sequence.append(" ")

    green_string = "".join(sequence)
    return green_string

#Generates a number of lines
def gen_read_buffer():
    buffer = list()
    counter = 1
    buffer.append(gen_random_sequence(0.05+(0.01*counter), None, True))
    for i in range(60):
        more_chars = random.randint(0,5)
        change_sequence = random.randint(0,10)
        if change_sequence == 0:
            buffer.append(gen_random_sequence(0.05+(0.01*counter)+(0.01*counter), None, True))
        elif more_chars == 0:
            buffer.append(gen_random_sequence(0.05+(0.01*counter), buffer[i], False))
            if 0.1+0.05*counter <= 0.7:
                counter+=0.3
        else:
            buffer.append(gen_random_sequence(0.05+(0.01*counter), buffer[i], False))
            counter-=0.1
    return buffer

while(True):
    read_buffer = gen_read_buffer()
    write_buffer = list()
    #Aqui si tenemos write_buffer listo deberia darnos el efecto deseado
    for line in read_buffer:
        write_buffer.append(line)
        for string in reversed(write_buffer):
            print("\033[1;34m "+string, flush=True)
        time.sleep(0.15)
        os.system("cls")
    read_buffer = list()
