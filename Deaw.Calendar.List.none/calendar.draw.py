# * sum,avg,min,max,flat
# * ploting
from mymethod import *
month_name  = "April"
days_name = ["Mo", "Tu", "Wd", "Th", "Fr", "Sa", "Su", ]
month_temps = [
    #   Mo  Tu   Wd   Th   Fr   Sa   Su        
    [ None,None,None,None, 5.0, 6.0, 7.0, ],    # |
    [  8.0, 7.0, 6.0, 5.0, 4.0, 3.0, 2.0, ],    # |
    [  1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, ],    # |
    [  8.0, 9.0, 8.0, 7.0, 6.0, 5.0, 4.0, ],    # < week
    [  3.0, 2.0, 1.0, 2.0, 3.0, 4.0,None, ]

]

########### display The Calendar #############
BoundaryBar()
print(f"| {month_name:54}|     |")
BoundaryBar()
#days names
for di in range(7):
    print(f"| {days_name[di]}    " , end="")
print("| Week|")    
BoundaryBar()
#days names

date = 1
# Temperatura pentru fiecare zi din saptamina
for wi in range(5):
    # Enumerarea zilelor din saptamina
    for di in range(7):
        if month_temps[wi][di] == None:
            date_str = " " * 6
        else:
            date_str = date
            date +=1    
        print(f"| {date_str:<6}", end="") 
    print("|     |") 
    # Enumerarea zilelor din saptamina
    # Enumerarea saptaminelor
    print("|       "*7,f"{wi+1:^5}|",sep= "|")
    # Enumerarea saptaminelor
    for di in range(7):
        if month_temps[wi][di] == None:
            temp = " "*6
        else:    
            temp = f"{month_temps[wi][di]:6.1f}"
        #temp = f"{month_temps[wi][di]:6.1f}" if month_temps[wi][di] != None else " " * 6            
        print(f"|{temp} " , end="")
    print(f"|     |")    
    BoundaryBar()
# Temperatura pentru fiecare zi din saptamina


########### display The Calendar #############
