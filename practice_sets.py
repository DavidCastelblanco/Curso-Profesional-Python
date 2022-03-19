def run():
    set1 = {1,9,6,7,'hola', 'chao'}
    set2 = {6,7,2,3,'chao'}

    set_union = set1 | set2
    print(set_union)

    set_intereseccion = set1 & set2
    print(set_intereseccion)

    set_diff = set1 -set2
    print(set_diff)

    set_diff_sim = set1 ^ set2
    print(set_diff_sim)


if __name__=='__main__':
    run()