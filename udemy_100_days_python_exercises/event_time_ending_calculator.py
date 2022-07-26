hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Write your code here.

end_hour= (hour*60+mins+dura//60)%24
end_minutes= (hour*60+mins+dura) % 60 

time= str(end_hour)+ ":"+ str(end_minutes)
print(time)