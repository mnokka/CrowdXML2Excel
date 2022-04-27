#
# Atlassian Crowd 3.7.0 backup file xml convertor
# processses file and creates two excels needed to import data to another Crowd
#
# This script generates two excels; user and group ones. Save them as "csv" (comma delimeter)
# Save also "empty" users csv file (just titles exists)
#
# In Crowd User import section:
# Phase 1: Import users and groups csv files (creates users and groups)
# Phase 2: Import Empty users and (normal) groups files (adds users to their groups)
#
# (c) 26.4.2022 mika.nokka1@gmail.com


import json
import xmltodict
import xlsxwriter


#hardcocde Atlassian Crowd 3.7.0 backup xml filename 
with open("backup.xml") as xml_file:
     
    data_dict = xmltodict.parse(xml_file.read())
    xml_file.close()

workbook1 = xlsxwriter.Workbook('1users.xlsx')
worksheet1 = workbook1.add_worksheet()
workbook2 = xlsxwriter.Workbook('2groups.xlsx')
worksheet2 = workbook2.add_worksheet()     

##################################################################
# User information excel creation

worksheet1.write(0,0,"UserName")
worksheet1.write(0,1,"FirstName")
worksheet1.write(0,2,"LastName")
worksheet1.write(0,3,"EmailAddress")
worksheet1.write(0,4,"Password")




len=(len(data_dict['crowd']['users']['user'])) # len works
row=1
column=0
for i in range(0,len):
    print ("NUMBER:{0}".format(i))
    #print (data_dict['crowd']['users']['user'][i])
    name=data_dict['crowd']['users']['user'][i]['name']
    firstName=data_dict['crowd']['users']['user'][i]['firstName']
    lastName=data_dict['crowd']['users']['user'][i]['lastName']
    email=data_dict['crowd']['users']['user'][i]['email']
    credential=data_dict['crowd']['users']['user'][i]['credential']
    print ("{0} {1} {2} {3} {4}".format(name,firstName,lastName,email,credential))
    
    worksheet1.write(row,column,name)
    worksheet1.write(row,column+1,firstName)
    worksheet1.write(row,column+2,lastName)
    worksheet1.write(row,column+3,email)
    worksheet1.write(row,column+4,credential)
    row=row+1
    
    print (".....................................................................")
    

###################################################################
# Group memberships excel creation
#
worksheet2.write(0,0,"UserName")
worksheet2.write(0,1,"GroupName")

counter=0 #len did not work with membership subdictionary
for i in data_dict['crowd']['memberships']['membership']:
    #print (i)
    counter = counter+1
    #print ("----------------------------------------------------------------------")

row=1
column=0    
for i in range(0,counter-1):
    print ("NUMBER:{0}".format(i))
    parentName=(data_dict['crowd']['memberships']['membership'][i]['parentName'])
    childName=(data_dict['crowd']['memberships']['membership'][i]['childName'])    
    print ("{0} {1}".format(parentName,childName))

    worksheet2.write(row,column,childName)
    worksheet2.write(row,column+1,parentName)
    row=row+1
    
    print (".......................................................................")


print ("User found:{0}".format(len))
print ("Directory memberships found:{0}".format(counter))


workbook1.close()
workbook2.close()