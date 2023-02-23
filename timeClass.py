# 6. Create a class Time with private attributes hour, minute and second. Overload ‘+’ operator
# to find sum of 2 times.

class time:
    def __init__(self,hour,minute,second):
        self.hour = hour
        self.minute = minute
        self.second = second
    def __add__(self,other):
        totalseconds = 0
        totalseconds += self.hour * 3600 + self.minute * 60 + self.second
        totalseconds += other.hour * 3600 + other.minute * 60 + other.second
        newH = totalseconds//3600
        newM = (totalseconds % 3600)//60
        newS = (totalseconds % 60)
        return time(newH,newM,newS)
    def displayTime(self):
        print(f'\n\n{self.hour}:{self.minute}:{self.second}')

h = int(input("Enter the hour for time 1: "))
m = int(input("Enter the minute for time 1: "))
s = int(input("Enter the second for time 1: "))
timea = time(h,m,s)

h = int(input("Enter the hour for time 2: "))
m = int(input("Enter the minute for time 2: "))
s = int(input("Enter the second for time 2: "))
timeb = time(h,m,s)

sumTime = timea+timeb   
sumTime.displayTime()

