import os
import random
import string
import time
from concurrent.futures import ThreadPoolExecutor

def file_generator(directory, number_of_files, size):
    os.makedirs(directory, exist_ok=True)
    for i in range(number_of_files):
        filename = os.path.join(directory, f'file{i}.txt')
        content = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=random.randint(size // 2, size)))
        with open(filename, 'w') as file:
            file.write(content)

def count_letters_in_file(filename, letter_to_find):
    with open(filename, 'r') as file:
        content = file.read()
        return content.count(letter_to_find)

def letter_counter_in_one_thread(directory, letter_to_find):
    count = 0
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            filepath = os.path.join(directory, filename)
            count += count_letters_in_file(filepath, letter_to_find)
    return count

def letter_counter_in_n_threads(directory, letter_to_find, number_of_threads):
    count = 0
    files = []
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            filepath = os.path.join(directory, filename)
            files.append(filepath)

    with ThreadPoolExecutor(max_workers=number_of_threads) as executor:
        results = executor.map(count_letters_in_file, files, [letter_to_find] * len(files))
        for result in results:
            count += result

    return count

def main():
    directory = 'files'
    number_of_files = 200
    file_size = 1000000
    letter_to_find = 'a'
    number_of_threads = 4

    # Generate files
    start_time = time.time()
    file_generator(directory, number_of_files, file_size)
    end_time = time.time()
    print(f"File generation time: {end_time - start_time} seconds")

    # Count letters in one thread
    start_time = time.time()
    count_single_thread = letter_counter_in_one_thread(directory, letter_to_find)
    end_time = time.time()
    print(f"Count in one thread: {count_single_thread}")
    print(f"Time taken in one thread: {end_time - start_time} seconds")

    # Count letters in multiple threads
    start_time = time.time()
    count_multi_thread = letter_counter_in_n_threads(directory, letter_to_find, number_of_threads)
    end_time = time.time()
    print(f"Count in {number_of_threads} threads: {count_multi_thread}")
    print(f"Time taken in {number_of_threads} threads: {end_time - start_time} seconds")

if __name__ == '__main__':
    main()
