#1. Declare an empty list
list=[]
print(list)

#2. Declare a list with more than 5 items
list_5i=['computer', 'apple', 'mouse','table','chair', 'school','tree']
print(list_5i)

#3. Find the length of your list
length=len(list_5i)
print(length)

#4. Get the first item, the middle item and the last item of the list
print(list_5i[0])
print(list_5i[3])
print(list_5i[-1])

#5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types=['Iván', '16','1.83','single','Jerez']

#6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon
it_companies=['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']

#7. Print the list using print()
print(it_companies)

#8. Print the number of companies in the list
print(len(it_companies))

#9. Print the first, middle and last company
print(it_companies[0])
print(it_companies[3])
print(it_companies[-1])

#10. Print the list after modifying one of the companies
it_companies[3]='Android'
print(it_companies)

#11. Add an IT company to it_companies
it_companies.append('Sony')
print(it_companies)

#12. Insert an IT company in the middle of the companies list
it_companies.insert(3, 'Activision')
print(it_companies)


#13. Change one of the it_companies item to uppercase
uppercase = it_companies[3].upper()
print(uppercase)

#14. Join the it_companies with a string '#;  '
join ='#,'.join(it_companies)
print(join)

#15. Check if a certain company exists in the it_companies list.
print('Sony' in it_companies)

#16. Sort the list using sort() method
it_companies.sort()
print (it_companies)

#17. Reverse the list in descending order using reverse() method
it_companies.reverse()
print (it_companies)

#18. Slice out the first 3 companies from the list
print (it_companies[0:3])

#19. Slice out the last 3 companies from the list
print(it_companies[0:6])

#20. Slice out the middle IT company or companies from the list
it_companies.pop(4)
print(it_companies)

#21. Remove the first IT company from the list
print(it_companies[1:7])

#22. Remove the middle IT company or companies from the list
it_companies.remove('Facebook')
print(it_companies)

#23. Remove the last IT company from the list
it_companies.remove('Activision')
print(it_companies)

#24. Remove all IT companies from the list
print(it_companies.clear())

#25. Destroy the IT companies list
del it_companies

#26. Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

#27. After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
Full=['Python', 'and SQL']
front_end.extend(Full)
front_end.extend(back_end)
print('Full stack:', front_end)
