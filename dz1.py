import random
import string

def generate_name(min_length=6, max_length=30):
    length = random.randint(min_length, max_length)
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

def generate_file(extension, min_length=6, max_length=30, min_bytes=256, max_bytes=4096, num_files=10):
    for i in range(num_files):
        file_name = generate_name(min_length, max_length) + '.' + extension
        file_size = random.randint(min_bytes, max_bytes)
        random_bytes = [random.randint(0, 255) for _ in range(file_size)]
        with open(file_name, 'wb') as file:
            file.write(bytes(random_bytes))

def generate_files(extensions, num_files):
    for extension, num_files in zip(extensions, num_files):
        generate_file(extension, num_files=num_files)

# Пример вызова функций
generate_file('txt')
generate_files(['txt', 'jpg', 'doc'], [10, 5, 3])