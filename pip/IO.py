#with open("FGT_OUTPUT", "w") as text_file:
#    text_file.write("Writing content to this file")

with open("FGT_OUTPUT") as text_file:
    lines = text_file.read(5)
    
print(lines)
