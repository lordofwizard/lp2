def main():
    # Define the string
    string = "\\Hello World"

    # Perform AND and XOR operations on each character
    print("Original String:", string)
    
    print("AND with 127:")
    and_result = ''.join(chr(ord(c) & 127) for c in string)
    print(and_result)

    print("XOR with 127:")
    xor_result = ''.join(chr(ord(c) ^ 127) for c in string)
    print(xor_result)

if __name__ == "__main__":
    main()
