lst = [10, 15, 3, 7, 2, 8, 6,-15,14,27, 45,86, 99,11, 12, 13, -10, 4]
def findmx(lst):
    peak = 0
    for elem in lst:
        if elem > peak:
            peak = elem
    print(peak)
findmx(lst)