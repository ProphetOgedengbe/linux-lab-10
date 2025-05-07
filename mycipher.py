#!/usr/bin/env python3
import sys

def caesar_cipher(text, shift):
    """
    Encrypt text using Caesar cipher with the given shift.
    Only encrypts uppercase A-Z letters, discards all other characters.
    """
    result = ""
    
    # Process each character in the input text
    for char in text:
        # Convert to uppercase
        char = char.upper()
        
        # Only process letters A-Z
        if 'A' <= char <= 'Z':
            # Apply shift and wrap around if necessary
            # ASCII value of 'A' is 65, 'Z' is 90
            shifted = ord(char) + shift
            
            # If we go past 'Z', wrap around to 'A'
            if shifted > 90:
                shifted -= 26
                
            result += chr(shifted)
    
    return result

def format_output(text):
    """
    Format the encrypted text in blocks of 5 letters, 10 blocks per line.
    """
    # Split the text into blocks of 5 characters
    blocks = [text[i:i+5] for i in range(0, len(text), 5)]
    
    # Group blocks into lines of 10 blocks each
    formatted_output = ""
    for i in range(0, len(blocks), 10):
        formatted_output += " ".join(blocks[i:i+10]) + "\n"
    
    return formatted_output.strip()

def main():
    # Check if shift value is provided
    if len(sys.argv) != 2:
        print("Usage: python3 mycipher.py <shift>")
        sys.exit(1)
    
    try:
        # Get the shift value from command line argument
        shift = int(sys.argv[1])
        
        # Make sure shift is between 0 and 25
        shift = shift % 26
        
        # Read input from stdin
        input_text = ""
        for line in sys.stdin:
            input_text += line
        
        # Apply Caesar cipher
        encrypted_text = caesar_cipher(input_text, shift)
        
        # Format and print output
        formatted_output = format_output(encrypted_text)
        print(formatted_output)
        
    except ValueError:
        print("Error: Shift must be an integer.")
        sys.exit(1)

if __name__ == "__main__":
    main()
