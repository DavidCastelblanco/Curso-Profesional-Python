
def is_palindrome(word: str) -> bool:
    word = word.replace(' ', '').lower()
    return word == word[::-1]

    
def run():
    word = print(input('Elige una palabra para saber si es un palindromo'))
    print(is_palindrome(word))

if __name__=='__main__':
    run()