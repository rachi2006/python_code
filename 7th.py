 #Dictionaries in python
print("\nDictionaries in python")
#famous cities in karnataka
dic = {
    "Bengalure" : "bisi bele bath",
    "Mysore" : "mysore pak",
    "Udupi" : "masala dosa",
    "Mangalore" : "neer dosa"
}

#accessing dictionary elements
print(dic["Udupi"])# Accessing value using key
print(dic.get("Mysore"))# Accessing value using get() method

#we can also add and update the dictionary elements
dic["Hubli"] = "jolad rotti"# Adding a new key-value pair
dic["Bengalure"] = "rava idli"# Updating an existing key-value pair

#we can also remove elements from the dictionary
New_dic = dic.pop("Mangalore")# Removing a key-value pair using pop()
print(New_dic) #or
#del dic["Udupi"]# Removing a key-value pair using del
#print(dic)
#dic.clear()# Clearing all elements from the dictionaryS
