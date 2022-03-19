def remove_duplicates(some_list):
    without_duplicates = []
    for i in some_list:
        if i not in without_duplicates:
            without_duplicates.append(i)
    return without_duplicates

def sets_remove_duplicate(some_list):
    set_list = set(some_list)    
    return list(set_list)
    

def run():
    random_list = [1,1,2,2,4]
    print(remove_duplicates(random_list))
    print(sets_remove_duplicate(random_list))

if __name__=='__main__':
    run()