fname = "feed.txt"

num_lines = 0
num_words = 0
num_chars = 0

with open(fname, 'r') as f:
    for line in f:
        words = line.split()

        num_lines += 1
        num_words += len(words)
        num_chars += len(line)
        
with open('words.txt', 'r') as file:
    file_contents = file.read()

    print('Total words:   ', len(file_contents.split()))
    print('total stops:    ', file_contents.count('.'))