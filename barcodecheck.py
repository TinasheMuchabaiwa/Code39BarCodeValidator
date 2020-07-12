# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 20:14:20 2020

@author: Syntegra
"""

mapping = {0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9', 10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F', 16:'G',
           17:'H', 18:'I', 19:'J', 20:'K', 21:'L', 22:'M', 23:'N', 24:'O', 25:'P', 26:'Q', 27:'R', 28:'S', 29:'T',
           30:'U', 31:'V', 32:'W', 33:'X', 34:'Y', 35:'Z', 36:'-', 37:'.', 38:' ', 39:'$', 40:'/', 41:'+', 42:'%'}

arr = '930431507W'
print('The barcode is : ', arr)

lst = list(arr)
lst2 = []

for i in range(0, 9, 1):
    lst2.append(int(lst[i]))
    
summedVal = sum(lst2)
print('\nStep 1: Sum of the first 9 characters is ', summedVal)

numCheckCharacter = summedVal % 43

print('\nStep 2: After dividing figure found in step 1 by 43, The check character is ',numCheckCharacter)

checkCharacter = (mapping[numCheckCharacter])

if (lst[9] == checkCharacter):
    print("\n",arr, " is a valid Barcode")
else:
    print("\n", arr, " is an Invalid Barcode")
