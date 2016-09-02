# Hint:  use Google to find python function
#import datetime library
from datetime import datetime

####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'   

#convert to Python datetime object
dt_start = datetime.strptime(date_start, "%m-%d-%Y")
dt_stop = datetime.strptime(date_stop, "%m-%d-%Y")

#evaluate difference
dt_diff = dt_stop - dt_start
print dt_diff

####b)  
date_start = '12312013'  
date_stop = '05282015'  

#convert to Python datetime object
dt_start = datetime.strptime(date_start, "%m%d%Y")
dt_stop = datetime.strptime(date_stop, "%m%d%Y")

#evaluate difference
dt_diff = dt_stop - dt_start
print dt_diff

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  

#convert to Python datetime object
dt_start = datetime.strptime(date_start, "%d-%b-%Y")
dt_stop = datetime.strptime(date_stop, "%d-%b-%Y")

#evaluate difference
dt_diff = dt_stop - dt_start
print dt_diff
