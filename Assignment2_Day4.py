def plot_histogram(dict1,design ="===",show=True,align=False):
    for key,value in dict1.items():
        if(show==True and align==False):
            print(f'{key} | {design*value} {value}') 
        elif(show==False and align==False):
            print(f'{key} | {design*value}')
        elif (show==True and align == True):
            space=int(max(dict1.values()))-value
            empt=" "
            print(f'{key} | {design*value} {empt*(space*len(design))} {value}') 

f={1:2,3:4,5:6}
plot_histogram(f,"***",show=True)