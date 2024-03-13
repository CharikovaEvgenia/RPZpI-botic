def upper_char(str, up_letter):
    char_list = list(str)
    for index in range(len(char_list)):
        if(char_list[index] == up_letter): 
            char_list[index] = char_list[index].upper()
    str = "".join(char_list)
    return str


str = 'lorem ipsum dolor sit amet, consectetur adipiscing elit. aenean tempus commodo diam, vel ornare tellus. morbi accumsan ante vel quam venenatis, vitae porta tortor accumsan. integer viverra'
print(upper_char(str, input()))