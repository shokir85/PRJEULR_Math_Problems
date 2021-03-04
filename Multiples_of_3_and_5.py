#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
#The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.
n =1000
def multiples_3and5(n):
    div3 = int((n-1)/3)
    div5 = int((n-1)/5)
    div15 = int((n-1)/15)
    smult3 = (3/2)*(1+ div3)*div3
    smult5 = (5/2)*(1+div5)*div5
    smult3and5 = (15/2)*(1+div15)*div15
    summ = smult3+ smult5 - smult3and5
    print(summ)
multiples_3and5(n)
    