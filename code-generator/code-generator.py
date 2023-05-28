# Create a code generator. This can that take text as input, replaces each letter with another letter, and outputs the “encoded” message.

def code_encoder(text):
    generated_code = text.replace("a", "e").replace("m", "o").replace("x", "y").replace("y", "m").replace("p", "y").replace("r", "0").replace("t", "p").replace("M", "n")
    return generated_code

code = input("What would you like to encode? ")
print(code_encoder(code))