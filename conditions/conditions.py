# PYTHON SUPPORTS USUAL LOGICAL COMPARISON CONDITIONS

# EQUALS ( == )
if 2 == 2:
    print('2 is equal to 2')

# NOT EQUALS ( != )
if 1 != 2:
    print('1 is not equal to 2')

# LESS THAN ( < )
if 1 < 2:
    print('1 is less than 2')

# LESS THAN OR EQUAL TO ( <= )
if 2 <= 2:
    print('2 is less than or equal to 2')

# GREATER THAN ( > )
if 3 > 2:
    print('3 is greater than 2')

# GREATER THAN OR EQUAL TO ( >= )
if 3 > 3:
    print('3 is greater than or equal to 3')


# ELIF IS A KEYWORD USED WHEN YOU NEED TO CHECK MORE THAN ONE CONDITION
# ELIF IS COMMONLY IMPLEMENTED AS "ELSE IF" IN OTHER PROGRAMMING LANGUAGES
# INTERPRET IT AS " IF THE PREVIOUS CONDITION WASN'T TRUE, TRY THIS ONE "

# ELSE WILL BE USED JUST IF ANY PREVIOUS CONDITION WERE SATISFIED
x = 10
y = 20
if x > y:
    print("x is greater than y")
elif x == y:
    print("x and y are equal")
else:
    print("y is greater than x")