def input_tuple_lc(prompt, types, sep):
    answer_str = input(prompt)
    new_list = answer_str.split(sep)
    new_tuple = ()
    if len(new_list) != len(types):
        print("Number of values inputted do not match number of values intended")
        return ()
    i = 0
    if len(new_list) == len(types):
        while i  < len(new_list): #or len(types)
            if i == len(new_list) - 1: #because bool('False') returns True, we use eval() instead
                try:
                    new_object = eval(new_list[i])
                    
                except NameError:
                    print("Error, incorrect data type inputted. If false/true typed, type Fale/True")
                    return ()
                new_tuple = new_tuple + (new_object,)
                i+=1
            else:
                try:
                    new_object = types[i](new_list[i])
                
                except ValueError:
                    print("Error, incorrect data type inputted")
                    return ()

                new_tuple = new_tuple + (new_object,)
                i+=1
        return new_tuple
    else:
        return ()
    
def input_tuple(prompt, types, sep):
    answer_str = input(prompt)
    converted_str = ''
    new_tuple = ()
    i = 0
    type_index = 0
    while i < len(answer_str) and type_index < len(types): #if answer_str has fewer elements than types, the new_tuple returned will have few intended elements, assuming there are no value errors
        if answer_str[i]==sep or i == len(answer_str) - 1:
            if i == len(answer_str)-1:
                converted_str = answer_str[:i+1]
                try:
                    converted_str = eval(converted_str)
                except NameError:
                    print("Error, incorrect data type inputted. If false typed, please type False")
                    return ()
            else: 
                converted_str = answer_str[:i]
                try:
                    converted_str = types[type_index](converted_str)
                except ValueError:
                    print("Error, incorrect data type inputted")
                    return ()
            
            new_tuple = new_tuple + (converted_str,)
            answer_str = answer_str[i+1:]
            i = 0
            type_index+=1
            
        else:
            i+=1
            
    return new_tuple

def read_tuple(file_obj, types, sep):
    new_str = ''
    for char in file_obj:
        new_str = new_str + char
    new_ls = new_str.split(' ') #get only the values we want
    new_str = new_ls[0]  #get the first element of the list 
    new_list = new_str.split(sep)
    new_tuple = ()
    if len(new_list) != len(types):
        print("Number of values inputted do not match number of values intended")
        return ()
    i = 0
    if len(new_list) == len(types):
        while i  < len(new_list): #or len(types)
            if i == len(new_list) - 1: #because bool('False') returns True, we use eval() instead
                try:
                    new_object = eval(new_list[i])
                    
                except NameError:
                    print("Error, incorrect data type inputted. If false/true typed, type Fale/True")
                    return ()
                new_tuple = new_tuple + (new_object,)
                i+=1
            else:
                try:
                    new_object = types[i](new_list[i])
                
                except ValueError:
                    print("Error, incorrect data type inputted")
                    return ()

                new_tuple = new_tuple + (new_object,)
                i+=1
        return new_tuple
        
    
sep = ','
prompt = "Please input a first name, last name, age, ID, and full-time(True or False) separated by '" + sep + "':"
types = (str,str,float,int,bool)
some_tuple = input_tuple(prompt,types,sep)
print(some_tuple)

some_tuple = input_tuple_lc(prompt,types,sep)
print(some_tuple)

file_obj = open("some_text.txt","r")
some_tuple = read_tuple(file_obj,types,sep)
print(some_tuple)
