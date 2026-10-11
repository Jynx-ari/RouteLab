#This file is quite noisy :>
import random

def generate_noisy(rows, cols, noise_level: int):
    generated_noise = set()
    noise_lvl = noise_level/10 
    for row in range(rows):
        for col in range(cols):
            rand_val = random.random()
            if rand_val < noise_lvl:
                generated_noise.add((row, col))
    return generated_noise
