import pandas as pd
import numpy as np
  

def validity_check():
    df = pd.read_csv('YourSourceCsvFile.csv')
    df.head()
    df.describe()
    columnToRead = df[['Barcode']]
    columnToRead.head()
    
    
    mapping = {0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9', 10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F', 16:'G',
           17:'H', 18:'I', 19:'J', 20:'K', 21:'L', 22:'M', 23:'N', 24:'O', 25:'P', 26:'Q', 27:'R', 28:'S', 29:'T',
           30:'U', 31:'V', 32:'W', 33:'X', 34:'Y', 35:'Z', 36:'-', 37:'.', 38:' ', 39:'$', 40:'/', 41:'+', 42:'%'}
    
    barcodes = np.asanyarray(columnToRead)
    
    x = []
    y = []
    z = []
    invalidBarcodes = []
    validBarcodes = []
    
    
    for i in range(0, len(barcodes)):
        if pd.isnull(barcodes[i][0])==False:
            x.append(barcodes[i][0])
            y.append(barcodes[i][0])
            
    for b in range(0, len(x)-1):
        x[b] = list(x[b])
        
        if len(x[b])<10:
            x[b].extend([' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])
           
    
    
    for j in range(0, len(x)-1):
        for w in range(0, 9):
            try:
                z.append(int(x[j][w]))
            except:
                z.append(x[j][w])
            if type(z[w]) is not int:
                z[w] = 0
                
        summedVal = sum(z)
        numCheckChar = summedVal%43
        checkChar = (mapping[numCheckChar])

        if checkChar == x[j][9]:
            validBarcodes.append(y[j])
        else:
            invalidBarcodes.append(y[j])
            
        z.clear()
    x.clear()
    inval = pd.DataFrame({'Invalid Barcodes':invalidBarcodes}) 
    val = pd.DataFrame({'Valid Barcodes':validBarcodes})
    val.to_csv('valid.csv', index=False)
    inval.to_csv('invalid.csv', index=False)
     
validity_check()
