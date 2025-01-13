pip install pyfiglet
import pyfiglet

def ascii_art_generator():
    print("ASCII Art Generator")
    print("-" * 30)
    
    # Get user input
    text = input("Enter the text to convert to ASCII art: ")
    
    # Create ASCII art using pyfiglet
    try:
        art = pyfiglet.figlet_format(text)
        print("\nGenerated ASCII Art:\n")
        print(art)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    ascii_art_generator()
