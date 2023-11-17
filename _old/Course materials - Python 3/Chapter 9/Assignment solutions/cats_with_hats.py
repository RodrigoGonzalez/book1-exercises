def get_cats_with_hats(array_of_cats):
    for num in range(1, 100+1):
        for cat in range(1, 100+1):
            if cat % num == 0:
                array_of_cats[cat] = array_of_cats[cat] is not True
    return [cat for cat in range(1, 100+1) if cats[cat] is True]

cats = [False] * (100+1)
print(get_cats_with_hats(cats))
