#Practice of regex
# regex used to match pattern with text.
# Symbol	   Meaning	                   Example	  Matches
#  .	Any character except newline	    a.c	      abc, a9c, a_c
#  \d	Any digit (0–9)	                   \d\d	      12, 45
#  \w	Any word character(letters,digits,_) \w+	  abc123
#  \s	Whitespace (space, tab, newline)	\s+	      ' '
#   ^	Start of string	                    ^Error	  “Error: failed login”
#   $	End of string	                    \.com$	  “example.com”
#   +	One or more	                         \d+	  1, 22, 333
#   *	Zero or more	                     a*0   	  '', a, aa, aaa
#   ?	Optional (0 or 1)	                 colou?r	color or colour
#  {n}	Exactly n times	                     \d{4}	    2025
#  {n,m} Between n and m times	            \d{2,4}	    20, 2025
#   []	 Character set	                     [aeiou]	any vowel
#  [^]	Negation (NOT these)	             [^0-9]	    any non-digit
#   `	`	                                   OR	    `cat
#  ()	 Grouping	                         (ab)+	    ababab
#  \b   Word Boundary Anchor                 \b\d{3}\b   (500,400,etc)
# \b ignores all the words and spaces any punctuation and wil match the pattern of any 3 digits in the text.


#import re
#text= "Login failed from 192.168.1.10 at 10:45AM"
#pattern=r"\d{3}\.\d{3}\.\d\.\d{2}+\s\w{2}\s\d{2}:\d{2}"
#result=re.findall(pattern,text)
#print(result)


#import re
#text = 'GET /index.html 200 OK\nGET /admin 403 Forbidden\nPOST /login 500 Error'
#pattern=r"\b\d{3}\b"
#result=re.findall(pattern,text)
#print(result)

import re
ip=r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"
time=r"\b\d{2}:\d{2}:\d{2}\b"

print("Paste your logs below. Once you are done please press Enter twice.")

log=""
while True:
    line = input()
    if line == "":
        break
    log += line + "\n"

ips=re.findall(ip,log)
times=re.findall(time,log)

print("\n       Log Analyzer      ")
print("IPs Found:",ips)
print("Times Found:",times)

