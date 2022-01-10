import os

# In Working

#Created at *.*.2021
#Last Update 10.01.2022

#Made by Neiki (Philipp Eckert)

#Private Github (https://github.com/EckertP)

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