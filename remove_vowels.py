# PROGRAM TO REMOVE VOWELS IN SBSTRINGS
str1=input("Enter the string:")
str2=""
for i in range(len((str1))):
    if str1[i] not in "aeiouAEIOU":
        str2=str2+str1[i]
print("Original string:",str1)
print("New string",str2)
