
all_time = 0
time = '1h 45m,360s,25m,30m 120s,2h 60s'
allt = time.replace(',', ' ').split()


for i in allt :
    if 'h' in i:
        time_h = int(i[:-1])
        all_time += time_h * 60
    elif 'm' in i:
        time_m = int(i[:-1])
        all_time += time_m
    elif 's' in i:
        time_s = int(i[:-1])
        all_time += time_s // 60 
   

        
    
   
    

print(all_time)


