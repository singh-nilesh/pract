# define the vector dictionary
vect_dict ={
    #    A  B  C  D
    "A":[0, 1, 1, 0],
    "B":[0, 0, 0, 0],
    "C":[0, 1, 0, 1],
    "D":[1, 0, 0, 0]
}
page_ids = {x:i for i,x in enumerate(vect_dict.keys())}

# Defining damping factor
DF = 0.85

# Initial page rank is 1
R = {"A":1, "B":1, "C":1, "D":1}

# Define the function for connection:
def connections(page):
    id = page_ids[page]
    incomings = []
    
    for i in vect_dict.keys():
        for con in range(len(vect_dict[i])):
            if vect_dict[i][con] == 1 and con == id:
                incomings.append(i)
    return incomings


# 