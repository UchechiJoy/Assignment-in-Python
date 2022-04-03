from re import M


my_list=[ "lucky", "Bright", "fumi"]
print(my_list[1])
my_list.append("Vero")
my_list[0]="Ini"
print(my_list)
my_list.insert(1, "Joy")
print(my_list)
my_list.remove("Ini")
print(my_list)
#To access last item in list
#Step 1
#length =len(my_list)
## step 2 : Deduct 1 from length to get the last index
#last_index=length- 1


my_dict={"id": 1, "name": "Lucky", "is_programmer": True, "salary": 1.2 ,"language": {"lang": "french" , "proficiency":100},{"lang": "Spanish", "proficiency":99}, "loans": { "package": "Student loan","amount": 10000}, { "package": "Student loan","amount": 10000} }
print (my_dict)
print(my_dict.get("loans")[1].get("package"))
print(my_dict.get ("name"))

my_set={"lucky", "funmi", " lucky", "Caleb", "Caleb"}
print(my_set)

my_tuple=("hello", "world")
print(my_tuple)