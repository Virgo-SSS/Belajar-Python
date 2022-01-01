# PROGRAM FOR LOOP

kotak = []
kotak.append(input("Masukan kalimat: "))

for i in kotak:
    score =  0
    print(i)
    for a in i:
        print(a)
        score += 1
    print("Total ejaan adalah :", score)


# kotak = ["apel"]
# i = apel