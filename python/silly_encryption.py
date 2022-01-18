import math

def silly_encryption(text:str):
    """
    An encyption algorithm.\n
    First, strip spaces in text, then arrange multiple rows of chars in a multidimensional array.\n
    The number of chars per row is determined by the (ceiling) square root of the length of the text.\n
    The encoded message is made by clumping each column of chars together and separating each clump with a space.\n
    """
    text,array = text.replace(" ",""),[]
    l = int(math.ceil(math.sqrt(len(text))))
    temp_list,temp_count = [],0
    for c in text:
        temp_list.append(c)
        temp_count += 1
        if temp_count % l == 0:
            array.append(temp_list)
            temp_count = 0
            temp_list = []
    while len(temp_list) < len(array[0]): temp_list.append(" ")
    array.append(temp_list)
    return " ".join(["".join(e).replace(" ","") for e in zip(*array)]).strip()