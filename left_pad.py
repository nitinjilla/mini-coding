# works same as npm left-pad(?)

def leftpad (string: str, length: int, char: str = " "):  

    pad = length - len(string)            
    return f"{(pad * str(char))[:pad]}{string}"

"""
print (leftpad('foo', 6, 0))    ==> 000foo
print (leftpad('foo', 6))       ==>    foo
print (leftpad('foo', 3, 0))    ==> foo
print (leftpad('foo', 6, 'a'))  ==> aaafoo
print (leftpad('foo', 6, 10))   ==> 101foo
"""