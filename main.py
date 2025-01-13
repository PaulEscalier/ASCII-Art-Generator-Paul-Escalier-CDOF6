from ascii_art_dict import ascii_art_dict

def generate_ascii_art(text):
    """Generate ASCII art for the given text."""
    text = text.upper()
    ascii_lines = [""] * 6  # Each character has 6 lines

    for char in text:
        char_art = ascii_art_dict.get(char, ["??????"] * 6)
        for i in range(6):
            ascii_lines[i] += char_art[i] + "  "  # Add spacing

    return "\n".join(ascii_lines)

def save_ascii_art_to_file(ascii_art, filename="ascii_art.txt"):
    """Save ASCII art to a text file."""
    with open(filename, "w") as file:
        file.write(ascii_art)
    return filename

if __name__ == "__main__":
    print("ASCII Art Generator\n")
    user_input = input("Enter text to convert to ASCII Art: ")
    ascii_art = generate_ascii_art(user_input)
    print("\nGenerated ASCII Art:\n")
    print(ascii_art)
    
    save_choice = input("\nVoulez-vous sauvegarder l'ASCII art dans un fichier texte? (oui/non): ").lower()
    if save_choice in ['oui', 'o', 'yes', 'y']:
        filename = input("Entrez le nom du fichier (ou appuyez sur Entrée pour utiliser 'ascii_art.txt'): ")
        filename = filename.strip() or "ascii_art.txt"
        if not filename.endswith('.txt'):
            filename += '.txt'
        saved_file = save_ascii_art_to_file(ascii_art, filename)
        print(f"\nASCII art sauvegardé dans '{saved_file}'")
