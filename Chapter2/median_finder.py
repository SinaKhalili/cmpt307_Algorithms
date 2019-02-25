import random

def find_median(values, select = -1):
    #This weird ternary just for the automatic select of a median
    select = len(values) / 2 + len(values) % 2 if select == -1 else select
    # Prints are commented out but useful to grasp algorithm
    # Insert array, will give median, lower on tie
    split = random.randint(0,len(values)-1)
    pivot = values[split]
    # print("Pivot is " + str(pivot))
    sl,sv,sr = [],[],[]
    for val in values:
        if(val < pivot):
            sl.append(val)
        elif(val == pivot):
            sv.append(val)
        else:
            sr.append(val)
    # print("ARRAY sl: ")
    # print(sl)
    # print("ARRAY sv: ")
    # print(sv)
    # print("ARRAY sr: ")
    # print(sr)
    # print("Select : " + str(select))
    if(select <= len(sl)):
        return find_median(sl, select)
    elif(select > len(sl) and select <= (len(sl) + len(sv))):
        return pivot
    else:
        return find_median(sr, select - len(sl) - len(sv))

