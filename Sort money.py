possible = [500,200,100,50,20,10,5,2,1,0.50,0.20,0.10,0.05,0.02,0.01]
li = []
index = len(possible)


def bills(ammount):
    counter = 0
    i = 0
    increment = 0
    while i < index:
        if possible[i] <= ammount- increment:
            li.append(possible[i])
            increment = increment + possible[i]
        else:
            i +=1


    for x in possible:
        index2 = 0
        while index2 < len(li):
            if li[index2] == x:
                counter += 1
            index2 +=1
        if not counter == 0:
            if x > 2:
                print(counter, x, "euro bills")
            else:
                print(counter, x, "euro coins")
        counter = 0
    
bills(float(input("input the ammount"))+0.01)
