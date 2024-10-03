
vowels = ['a', 'e', 'i' ,'o' ,'u', 'A', 'E', 'I', 'O', 'U']


def main():
    user_input = input('input: ')
    twttr = shorten(user_input)
    print(f'output: {twttr}')

def shorten(word):
    for vowel in vowels:
        word = word.replace(vowel, '')
    return word

if __name__ == "__main__":
    main()
