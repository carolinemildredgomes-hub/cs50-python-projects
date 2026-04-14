
---

---

# 📘 2) `watch` Project README

```markdown
# ▶️ YouTube Embed URL Converter (WATCH)

A CS50-style Python project based on **Regular Expressions and HTML Parsing**.

This project extracts a YouTube video ID from an embedded iframe URL and converts it into a shareable `youtu.be` link.

---

## 📌 Project Objective

Convert HTML iframe embed links like:

```text
https://www.youtube.com/embed/xvFZjo5PgG0

into:

https://youtu.be/xvFZjo5PgG0

📌 Features
HTML iframe parsing
src attribute extraction
regex capture groups
optional http / https / www
short URL conversion

📌 Concepts Used
re.search()
capturing groups
optional regex patterns
f-strings

📌 How It Works
Searches HTML for iframe src
Extracts video ID using regex
Builds short shareable YouTube URL
Returns None if invalid

📌 Run Project
python watch.py

📌 Example
HTML: <iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>
https://youtu.be/xvFZjo5PgG0


📌 Learning Outcome

This project improves understanding of:

regex extraction
HTML string parsing
URL manipulation
