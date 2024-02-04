from replit import db
import datetime, os, time

password = "WarisPeace"
def addDiary():
  time.sleep(1)
  os.system("clear")
  timestamp = datetime.datetime.now()
  print(f"Diary entry for {timestamp}")
  print()
  entry = input("> ")
  db[timestamp] = entry
def viewDiary():
  keys = db.keys()
  for key in keys:
    time.sleep(1)
    os.system("clear")
    print(f"""{key}
    {db[key]}""")
    print()
    opt = input("Next or exit? > ")
    if(opt.lower()[0]=="e"):
      break
userInput = input("What's the password?")
if userInput != password:
  print("Wrong!")
  exit()
while True:
  print("Accessing Diary OS v24...")
  time.sleep(2)
  optionInput = input("\n Option 1. Add Diary\n Option 2. View Diary\n >")
  if optionInput == "1":
    addDiary()
  elif optionInput == "2":
    viewDiary()
  else:
    print("That is not an option!")
  