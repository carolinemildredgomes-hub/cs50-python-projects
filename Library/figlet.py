import sys
import random
from pyfiglet import Figlet

figlet = Figlet()

# Check command-line arguments
if len(sys.argv) == 1:
    # No arguments → random font
    fonts = figlet.getFonts()
    random_font = random.choice(fonts)
    figlet.setFont(font=random_font)

elif len(sys.argv) == 3:
    # Must be -f or --font
    if sys.argv[1] not in ["-f", "--font"]:
        sys.exit("Invalid usage")

    font_name = sys.argv[2]

    # Check if font exists
    if font_name not in figlet.getFonts():
        sys.exit("Invalid font")

    figlet.setFont(font=font_name)

else:
    sys.exit("Invalid usage")

# Get user input
text = input("Input: ")

# Print styled text
print(figlet.renderText(text))
