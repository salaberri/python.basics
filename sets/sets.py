# PYTHON IMPLEMENTS FOUR DIFFERENT TYPES OF COLLECTIONS [ LISTS, TUPLES, SETS, DICTIONARY ]
# SETS : UNORDERED, UNINDEXED AND DON'T ALLOW DUPLICATED MEMBERS
mySet = {"AAA", "BBB"}
print(mySet)


# CHECK NO DUPLICATES BEHAVIOR
duplicatedSet = {"AAA", "AAA", "BBB", "BBB", "CCC"}
print(duplicatedSet)


# CREATE A LIST USING SET CONSTRUCTOR
colorSet = set(("BLUE", "WHITE", "RED"))
print(colorSet)


# ADD AN ITEM
basicSet = {"FIRST", "SECOND"}
basicSet.add("THIRD")
print(basicSet)


# REMOVE AN ITEM
bigSet = {1, 2, 5, 7}
bigSet.remove(5)
print(bigSet)


# NUMBER OF ITEMS IN A SET
numbersSet = {1, 3, 5, 7, 9, 11}
print(len(numbersSet))