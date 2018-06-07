# LOOPS ARE USED TO ITERATE OVER A SEQUENCE ( LISTS, TUPLES, STRINGS )
# FOR
# ITERATES OVER A SEQUENCE
colors = ["BLUE", "RED", "GREEN"]
for color in colors:
    print(color)

# WHILE
# ITERATE UNTIL THE CONDITION IS TRUE
index = 1
while index < 6:
    print(index)
    index = index + 1

# SPECIAL WORDS/STATEMENTS
# BREAK : USED TO STOP THE LOOP ITERATION BEFORE IT ENDS
colors = ["BLUE", "RED", "GREEN"]
for color in colors:
    if color == "RED":
        break
    print(color)

# CONTINUE : USED TO STOP CURRENT ITERATION AND JUMP RIGHT TO THE NEXT
colors = ["BLUE", "RED", "GREEN"]
for color in colors:
    if color == "BLUE":
        continue
    print(color)