theCats = {i: False for i in range(1, 101)}
for i in range(1, 101):
    for cats in theCats:
        if cats % i == 0:
            theCats[cats] = not theCats[cats]
for cats, value in theCats.items():
    if value:
        print(f"Cat {cats} has a hat.")
    else:
        print(f"Cat {cats} is hatless!")
