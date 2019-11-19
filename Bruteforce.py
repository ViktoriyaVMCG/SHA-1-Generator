import hashlib #hashlib Secure hashes and message digests, algorithms SHA1, SHA224, SHA256, SHA384, and SHA512

import bcrypt as bcrypt #bcryot адаптивная криптографическая хеш функция формирования ключа
bcrypt
password = input("Input the password to hash\n")
print("\nSHA1:\n")
for i in range(3):

    #распространённый стандарт кодирования текста, позволяющий более компактно хранить
    # и передавать символы Юникода, используя переменное количество байт, и обеспечивающий
    # полную обратную совместимость с 7-битной кодировкой ASCII.

    #UTF-8 is a variable width character encoding capable of encoding
    # all 1,112,064 valid code points in Unicode using one to four 8-bit bytes.
    setpass = bytes(password,'utf-8') # to generate 16 or 32 just change the 8
    hash_object = hashlib.sha1(setpass) # here we mention that it will use sha1
    guess_pw = hash_object.hexdigest() #hexdigest return a str
    print(guess_pw)