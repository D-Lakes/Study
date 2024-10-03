input = input('input: ')

vowels = ['a', 'e', 'i' ,'o' ,'u', 'A', 'E', 'I', 'O', 'U']

for vowel in vowels:
    input = input.replace(vowel, '')

print(f'output: {input}')
