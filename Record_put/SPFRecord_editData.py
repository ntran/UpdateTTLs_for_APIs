import string

def SPFRecord_editData(string):

    length = len(string) - 1
    i = length

    while i >= 0:
        if string[i] == '\\' or string[i] == '"' or string[i] == ';':
            if i == 0:
                string = '\\' + string
                i -= 1
            else:
                if string[i-1] != '\\':
                     string = string[:i] + '\\' + string[i:(length+1)]
                     length += 1
                     i -= 1
                else:
                    i -= 2
        else:
            i -= 1
    return string

