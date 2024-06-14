#Used in creating privacy encrypting engine for text and data
#Try using decryption software too

def crypted (sentence):
    translation=""
    for element in sentence:
        if element in "Aa":
            translation=translation+"!"
        elif element in "Bb":
            translation=translation+"@"
        elif element in "Cc":
            translation=translation+"#"
        elif element in "Dd":
            translation=translation+"$"
        elif element in "Ee":
            translation=translation+"%"
        elif element in "Ff":
            translation=translation+"&"
        elif element in "Gg":
            translation=translation+"*"
        elif element in "Hh":
            translation=translation+"("
        elif element in "Ii":
            translation=translation+")"
        elif element in "Jj":
            translation=translation+"_"
        elif element in "Kk":
            translation=translation+"+"
        elif element in "Ll":
            translation=translation+"="
        elif element in "Mm":
            translation=translation+"{"
        elif element in "Nn":
            translation=translation+"}"
        elif element in "Oo":
            translation=translation+"|"
        elif element in "Pp":
            translation=translation+"]"
        elif element in "Qq":
            translation=translation+":"
        elif element in "Rr":
            translation=translation+";"
        elif element in "Ss":
            translation=translation+"."
        elif element in "Tt":
            translation=translation+"/"
        elif element in "Uu":
            translation=translation+">"
        elif element in "Vv":
            translation=translation+","
        elif element in "Ww":
            translation=translation+"?"
        elif element in "Xx":
            translation=translation+"~"
        elif element in "Yy":
            translation=translation+"`"
        elif element in "Zz":
            translation=translation+"["
        else:
            translation=translation+element

    return translation
           
print(crypted(input("What do you want to crypt")))