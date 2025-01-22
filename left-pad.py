# hope to break production some day

def leftpad (string, pad_count, char = " "):

    padding = pad_count - len(string)
    return f"{padding * str(char)}{string}"

# print (leftpad('foo', 6, 0))    ==> 000foo
# print (leftpad('foo', 6))       ==>    foo
# print (leftpad('foo', 3, 0))    ==> foo
# print (leftpad('foo', 6, 0))    ==> 000foo