vowels = ['a', 'e', 'i', 'o', 'u']
word = input("Provide a word to search for vowels: ")
found = {}
for letter in word:
    if letter in vowels:
        found.setdefault(letter, 0) #设置初始值，相当于判断key是否在found中
        found[letter] += 1
for k, v in found.items():
    print(k, 'was found', v, 'time(s).')
