email = input("What's your email? ").strip()

username , domain = email.split("@")

if username  and "." in domain:
    print("Valid")
else:
    print("Invalid")

Another method

import re

email = input("What's your email? ").strip()

if re.search("@",email):
    print("Valid")
else:
    print("Invalid")

