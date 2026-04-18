# CS50 Shirtificate 🎓👕

**CS50 Python — PDF Generation Project**

This project generates a personalized **CS50 Shirtificate (PDF)** using the `fpdf2` library. The certificate includes a CS50 shirt image and overlays the user’s name on top of it.

---

## Features

* Generates a PDF in **A4 Portrait format**
* Displays title: **CS50 Shirtificate** at the top
* Centers the shirt image horizontally
* Places user’s name on the shirt in white text
* Clean and simple layout

---

## Project Structure

```text
shirtificate.py
shirtificate.png
shirtificate.pdf
README.md
```

---

## Requirements

Install the required library:

```bash
pip install fpdf2
```

---

## How It Works

* The program asks for the user’s name
* Creates a PDF page (A4 size, portrait orientation)
* Adds a title at the top
* Inserts the shirt image in the center
* Writes the user’s name on the shirt image
* Saves the file as `shirtificate.pdf`

---

## Usage

```bash
python shirtificate.py
```

Then enter your name when prompted.

---

## Output

A file named:

```text
shirtificate.pdf
```

will be created in your directory.

---

## Concepts Used

* PDF generation with `fpdf2`
* Positioning elements (text + images)
* Working with coordinates in a document
* User input handling

---

## Author

**Caroline Mildred Gomes**

---

## Notes

* Ensure `shirtificate.png` is in the same directory as the script
* Long names are not wrapped automatically
* Layout can be customized further with colors, borders, or fonts
