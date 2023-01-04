# Import the module 
import re

text = """
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

need to be escaped
. ^ $ * + ? { } [ ] \ | ( )

Mr. Verma

#ffff89

contact.rskcode@gmail.com
test@university.edu
armylover321@yahoo.net

https://www.google.com
http://passthepillow.netlify.app
HTTPS://YOUTUBE.COM
https://www.isro.gov.in
https://www.isro2.in
Go to the url - lensa.ai



321*987*4321
321-987-4321
995.342.2341
9953422341
category cat catch
"""
# text = "ct cat caat caaat caaaat"

# Find Email IDs
# Find All the urls in a given string 
# find Mobile number 

# pattern = re.compile(r'[a-zA-Z0-9\.]+@[\w\.]+[a-zA-Z]')
pattern = re.compile(r'((http|https|HTTP|HTTPS):\/\/)([www\.]?[\w\.]+[a-zA-Z]+)')
# pattern = re.compile(r'\s[\w]+[\.][\w]+\s')
# pattern = re.compile(r'\d\d\d[\.|\-]?\d\d\d[\.|\-]?\d\d\d\d')
# pattern = re.compile(r'ca*t')

matches = pattern.finditer(text)

for match in matches:
    print(f"Match starts at {match.start()}. Match is {match.group(3)}")






