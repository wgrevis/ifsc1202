print("Price    Change")
def percentchange(today,yesterday):
    return ((float(today) - float(yesterday)) / float(yesterday)) * 100

demotextfile = open("06.02 Stock.txt", "r")

yesterday = demotextfile.readline().strip()
print(yesterday)
today = ""

while yesterday != "":
  if today == "":
    today = demotextfile.readline().strip()
    continue
  print("{:2}      {:.3}%".format(today,(percentchange(today,yesterday))))
  #print(today + "    " + str(percentchange(today,yesterday)))
  yesterday = today
  today = demotextfile.readline().strip()
  if today == "":
    break
  #print("today: " + today + "    yesterday: " + yesterday)
  
demotextfile.close()
