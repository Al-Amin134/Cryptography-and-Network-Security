def encryption(text, width):
    while(len(text)%width!=0):
        text+="_"
    rows = []
    for i in range(0, len(text), width):
        rows.append(text[i:i+width])
        result = ""
        for i in range(width):
            for row in rows:
                result+=(row[i])
    return result
def decryption(cipher, width):
    result = ""
    height = len(cipher)//width
    cols = []
    for i in range(0, len(cipher), height):
        cols.append(cipher[i:i+height])

    for i in range(height):
        for col in cols:
            result+=col[i]
    return result
text = "University of Rajshahi"
width = 3
c = encryption(text, width)
p = decryption(c, width)
p = p.rstrip("_")
print(c)
print(p)