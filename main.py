from ascii_art_dict import ascii_art_dict

def generate_ascii_art(text):
    """Generate ASCII art for the given text."""
    text = text.upper()
    ascii_lines = [""] * 6  # Each character has 6 lines

    for char in text:
        if char == " ":
            for i in range(6):
                ascii_lines[i] += "      "  # 6 espaces
            continue
            
        char_art = ascii_art_dict.get(char, ["??????"] * 6)
        for i in range(6):
            ascii_lines[i] += char_art[i] + "  "  # Add spacing

    return "\n".join(ascii_lines)

if __name__ == "__main__":
    print("ASCII Art Generator\n")
    user_input = input("Enter text to convert to ASCII Art: ")
    print("\nGenerated ASCII Art:\n")
    print(generate_ascii_art(user_input))
