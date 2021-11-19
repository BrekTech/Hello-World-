print("K- Hello You!\nMy name is Kevin.")
print("What is your name?")
print()

name =input()
print()

if name == "Kevin" or name == "kevin":
  name="Kevin"
  print("Wow, we got the same name. Hi there Kevin")
  
else:
  print(f"K- Hi there {name}")

print("How old are you?" )
print()

age=input()
print()

print("K- Why are you "+age+"?")
print()

NotImportant= input()
print()

print("K- You are strange "+name)
print("Do you like hats?")
print()

Stance_on_hats= input() 
print()

if Stance_on_hats == "Yes"or Stance_on_hats =="yes" :
  Stance_on_hats = "like"
  pass
else:
  if Stance_on_hats == "No"or Stance_on_hats=="no":
    Stance_on_hats = "dislike"
    pass
  else: 
    Stance_on_hats = "NA"

print("K- I agree")

if name == "Kevin":
  print ("One last question. Are you having a good day?")
  print() 
  pass
else:
  print("What\'s your name again?")
  print()
  
  previous_input=input()
  print()

  if name == previous_input: 
    print ("K- One last question. Are you having a good day?")
    print()
    pass
  else: 
    print(f"K- Liar!!! You said your name was {name}! \nYou can't trick me \nSo which one is it? {name} or {previous_input}?")
    print()

    name_choice=input()
    print()
    if name_choice == name:
      name = name 
      print ("K- One last question. Are you having a good day?")
      print()
      pass

    else:
      if name_choice == previous_input:
        name = previous_input
        print ("K- One last question. Are you having a good day?")
        print()
        pass 
      
      else:
        print(f"K- No, you only got 2 options. {name} or {previous_input}. Which one is it?")
        print()

        name_choice=input()
        print()

        if name_choice == name: 
          print (f"K- Ok then, your name is {name}")
          pass
        
        else: 
          if name_choice == previous_input:
            name = previous_input
            print (f"K- Ok then, your name is {name}")
            pass
          
          else:
            print("K- Whatever, I will just call you Smith")
            name = "Smith"
        print ("One last question. Are you having a good day?")
        print()          


Opinion_on_day=input()
print()

if Opinion_on_day == "Yes"or Opinion_on_day =="yes" :
  print("K- That's Wonderful!")
  Opinion_of_day = "good day"
  pass
else:
  if Opinion_on_day == "No"or Opinion_on_day =="no":
    print("K- I'm sorry to hear that" )
    Opinion_of_day = "bad day"
    pass
  else: 
    print("K- Interesting.")
    Opinion_of_day = "NA"

print()
print(f"SUMMARY...\nYour name is {name}.\nYou are {age} years old.")
if Opinion_of_day == "NA":
  pass
else:
  print(f"You are having a {Opinion_of_day}.")
if Stance_on_hats == "NA":
  pass
else:
  print(f"And you {Stance_on_hats} hats.")