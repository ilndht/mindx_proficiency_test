def merge2String(str1,str2):
    final_string = ''
    if len(str2)> len(str1):
        k = len(str1)
    else :
        k =  len(str2)
    for i in range(k): 
        final_string=final_string+ str1[i]+str2[i]
    if len(str2)> len(str1): 
        final_string += str2[len(str1):]
    if len(str1)> len(str2): 
        final_string += str1[len(str2):]
    return final_string
