def num_count(f):
    num_words = len(f.split())
    print(f"Found {num_words} total words")
    return num_words


def alpha_count(f):
    f = f.lower()
    words_array =f.split(" ")
    dict = {'a': 0 , 'b':0 , 'c':0, 'd' :0 , 'e' :0 , 'f' :0, 'g' :0, 'h' :0 ,'i':0 ,'j':0 ,'k' :0,'l':0 ,'m':0, 'n':0 ,'o':0, 'p':0 ,'q':0 ,'r':0, 's':0 ,'t':0 ,'u':0 ,'v':0 ,'w':0 ,'x':0 ,'y':0 ,'z':0 , 'æ':0 ,'â': 8 ,
'ê': 0 , 'ë': 0 , 'ô': 0 }

    for word in words_array:
        for letter in word :
            try:
                dict[letter]+=1
            except Exception:
                pass    
        
    return dict


def helper_function(items):
    return items["num"]


def sorted_list_of_dict(dict):
    letters = "abcdefghijklmnopqrstuvwxyzæâêëô"

    list_of_dict =[]
    for i in range(len(dict)):
        dicti={}
        dicti["char"] = letters[i]
        dicti["num"] = dict[letters[i]]
        list_of_dict.append(dicti)
    list_of_dict.sort(reverse=True , key = helper_function)

    return list_of_dict
        


