import os

def main():
    plaintext = input('Input here your Text: ')
    if not plaintext:
        input("Plain Text field was Empty")
    end_output = " ".join(f"{ord(i):08b}" for i in str)
    print(end_output)
    
try:
    main()
except KeyboardInterrupt:
    exit()
except Exception as Error:
    print(Error)