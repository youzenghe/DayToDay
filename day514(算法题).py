from fractions import Fraction
from datetime import *
# def sums(n):
#     su = Fraction(0)
#     for i in range(0,n):
#         su += Fraction(1,2**i)
#     print(su)

# def method():
#     cnt = 0
#     i = 0
#     while True:
#         cnt+=str(i).count("1")
#         if cnt>=2021:
#             print(i)
#             break
#         i+=1

# def oneway(*args):
#     dt = datetime(*args)
#     return dt
# def twoway(n,m):
#     return abs(n-m).days

# def newway(year)不使用:calendar
#      list1 = [1,3,5,7,8,10,12]
#      list2 = [4,6,9,11]
#      con = 0
#      if year%4 == 0 and year%100 != 0 or year%400 == 0:
#          day  = 29
#      else:
#          day = 28
#      for i in list1:
#           i = str(i).zfill(2)
#           for j in range(1,32):
#                j = str(j).zfill(2)
#                ij = i+j
#                if int(ij[0]) == int(ij[1])-1 and int(ij[1]) == int(ij[2])-1 or int(ij[1]) == int(ij[2])-1 and int(ij[2]) == int(ij[3])-1:
#                     con+=1
     
#      for j in range(1,day+1):
#          i = "02"
#          j = str(j).zfill(2)
#          ij = i+j
#          if int(ij[0]) == int(ij[1])-1 and int(ij[1]) == int(ij[2])-1 or int(ij[1]) == int(ij[2])-1 and int(ij[2]) == int(ij[3])-1:
#             con+=1
#      for i in list2:
#          i = str(i).zfill(2)
#          for j in range(1,31):
#             j = str(j).zfill(2)
#             ij = i+j
#             if int(ij[0]) == int(ij[1])-1 and int(ij[1]) == int(ij[2])-1 or int(ij[1]) == int(ij[2])-1 and int(ij[2]) == int(ij[3])-1:
#                con+=1
#      print(con)
def num():
   num = 1000000007
   num2 =  999999999
   # for i in range(1,num+1):
   #     if i*2021%num == num2:
   #         print(i)
   #         return
   while 1:
       if num//2021>num2:
           break
       if num2 % 2021 == 0:
           print(num2//2021)
           return
       num2+=num
   print(0)
if __name__ == '__main__':
    # sums(20)
    # method()
#    print(datetime(1901,1,1).weekday()+1)
#    day =  float(twoway(oneway(1901,1,1),oneway(2000,12,31))/7)
#    print("%.1f"%day)
    #  newway(2022)
    num()