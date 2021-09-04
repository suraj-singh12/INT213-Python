# Nested for loops / patterns
'''
    print this pattern: 

    *
    **
    ***
    ****
'''
rows = range(1,5)                # as we have 4 rows
for row in rows:       
    for star in range(0,row):    # as we have i stars everytime
        print("*",end = "")
    print()

