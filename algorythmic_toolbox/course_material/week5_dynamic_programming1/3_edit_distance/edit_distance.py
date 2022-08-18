# Uses python3
def edit_distance(s, t):
    
    assert all([x in 'abcdefghijklmnopqrstuvwxyz' for x in s]), \
        'All characters of s must be small Latin'
    
    assert all([x in 'abcdefghijklmnopqrstuvwxyz' for x in t]), \
        'All characters of s must be small Latin'

    m = len(s)
    n = len(t)
    
    sub_solutions = [[0 for x in range(n + 1)] for x in range(m + 1)]
    
    # with help of https://www.geeksforgeeks.org/edit-distance-dp-5/
    for ii in range(m + 1):
        for kk in range(n + 1):
 
            # If first string is empty, only option is to
            # insert all characters of second string
            if ii == 0:
                sub_solutions[ii][kk] = kk    # Min. operations = j
 
            # If second string is empty, only option is to
            # remove all characters of second string
            elif kk == 0:
                sub_solutions[ii][kk] = ii    # Min. operations = i
 
            # If last characters are same, ignore last char
            # and recur for remaining string
            elif s[ii-1] == t[kk-1]:
                sub_solutions[ii][kk] = sub_solutions[ii-1][kk-1]
 
            # If last character are different, consider all
            # possibilities and find minimum
            else:
                sub_solutions[ii][kk] = 1 + min(sub_solutions[ii][kk-1],      # Insert
                                              sub_solutions[ii-1][kk],      # Remove
                                              sub_solutions[ii-1][kk-1])    # Replace
    
    return sub_solutions[m][n]

if __name__ == "__main__":
    DEBUG = not True
    if not DEBUG:
        print(edit_distance(input(), input()))
    else:
        T = (('Hello World',
              'Hello Elon'),
             ('ab',
              'ab'),
             ('short',
              'ports'),
             ('editing',
              'distance'),
             ('firststring',
              'secondstring'),
             ('sunday',
              'saturday')
             )
        for n in range(len(T)):
            try:
                print('%d: %d' % (n, edit_distance(T[n][0], T[n][1])))
            except:
                print('%d: failed' % n)
