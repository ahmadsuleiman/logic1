def cigar_party(cigars, is_weekend):
  return cigars>=40 and is_weekend or cigars>=40 and cigars<=60
  
def date_fashion(you, date):
  if you<=2 or date<=2:
    return 0
  if you>=8 or date>=8:
    return 2
  return 1
  
def squirrel_play(temp, is_summer):
  return temp>=60 and temp<=90 or temp>=60 and temp<=100 and is_summer
  
def caught_speeding(speed, is_birthday):
  if speed<=60 or is_birthday and speed<=65:
    return 0
  if speed>=61 and speed<=80 or is_birthday and speed>=66 and speed<=85:
    return 1
  if speed>=81 or is_birthday and speed>=66 and speed<=85:
    return 2
	
def sorta_sum(a, b):
  if a+b>=10 and a+b<=19:
    return 20
  return a+b
  
def alarm_clock(day, vacation):
  if day>=1 and day<=5 and not vacation:
    return "7:00"
  elif day>=1 and day<=5 and vacation:
    return "10:00"
  elif (day==0 or day==6) and not vacation:
    return "10:00"
  return "off"
  
def love6(a, b):
  return a==6 or b==6 or a+b==6 or abs(a-b)==6
  
def in1to10(n, outside_mode):
  return outside_mode and n not in range(2,10) or not outside_mode and n in range(1,11)
  
def near_ten(num):
  return num%10+2>=10 or num%10-2<=0
  
