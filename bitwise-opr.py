# program to demonstrate the bitwise operators

plays = {
"Ant and Cleo": "Ant is there, Brutus is Caeser is with Cleo mercy worser.",
"Julius Caeser": "Ant is there, Brutus is Caeser is but Calpurnia is.",
"The Tempest": "mercy worser",
"Hamlet": "Caeser and Brutus are present with mercy and worser",
"Othello": "Caeser is present with mercy",
"Macbeth": "Ant is there; Caeser, mercy."
}

words = ['Ant', 'Brutus', 'Caeser', 'Calpurnia', 'Cleo', 'mercy', 'worser']

# matrix creation -- matrix[words, plays]
matrix = [ [0 for _ in range(len(plays))] for _ in range(len(words))]

text_list = list(plays.values())

# creating vector matrix
for i in range(len(words)):
    for j in range(len(plays)):
        
        if (words[i] in text_list[j]): # check for each word in play( row-wise )
            matrix[i][j] = 1
        else:
            matrix[i][j] = 0

# Printing the vector matrix headings
print(f"{ ' word  \\  play':<15}", end='\t')
for play_name in plays.keys():
    print(f"{play_name:<12}", end='\t')
print()

# Printing the vector matrix data
for i in range(len(words)):
    print(f"{words[i]:<15}", end='\t')
    
    for j in range(len(plays)):
        print(f"{matrix[i][j]:<12}", end='\t' )
    print()
        
print("----- "*20) # -----------

# Generating binary presence as integers
vector_dict = {}
for id,vector in enumerate(matrix):
    myStr = ''.join(str(x) for x in vector)
    vector_dict[words[id]] = int(myStr,2)

print(f" Binary presence as integers : \n", vector_dict)

print("----- "*20) # -----------

# Accepting condition as input
orgCondition = condition = input(f" Enter your condition: \n Use only {words} \n\t > ")

# Replace words --> binary integer representation
for word in words:
    if word in condition: 
        condition = condition.replace(word, str(vector_dict[word]))

print(f" Binary corresponding integer representation : {condition}")

print("----- "*20) # -----------

# Replace logical operations
condition = condition.replace("not", "and~").replace("or", "|").replace("and", "&")

# Evaluate
try:
    evalStr = bin(eval(condition)).replace("0b", '') # Convert to binary
    print(" Binary string form : ",evalStr)
    print("----- "*20) # -----------

    # Main
    print(" The plays which satisfy the condition", condition, "are :")

    for i,char in enumerate(evalStr):
        if char == '1':
            print("\t =>", list(plays.keys())[i])
except NameError:
    print("Use only ",words)
except:
    print("Error !!!!")

