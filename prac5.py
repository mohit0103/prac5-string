p=input("Enter your word/sentence: ")
long=0
for i in p.split():
  if (len(i) > long):
    long = len(i)
print(f"longest word has {long} characters.")

char = input("Enter which character to be counted: ")
cnt = 0
cnt1 = 0
for i in p:
  cnt=cnt+1
print("Total characters in the string is", cnt)

for i in p:
  if (i==char):
    cnt1 = cnt1+1
print(f"This letter has occured {cnt1} times.")

q=""
for i in p:
  q=i+q
if q==p:
  print("This is a Palindrome.")
else:
  print("This is NOT a Palindrome.")

r=input("Enter substring to be checked: ")
if r in p:
  print("This substring EXISTS.")
else:
  print("This substring DOESN'T EXIST")
