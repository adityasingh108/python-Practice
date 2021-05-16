import pywhatkit
a = pywhatkit.text_to_handwriting("""Python (programming language)
From Wikipedia, the free encyclopedia
Jump to navigationJump to search
For other uses, see Python (disambiguation).
Python """,rgb=(0,0,255))
print(a)
print(help(pywhatkit))