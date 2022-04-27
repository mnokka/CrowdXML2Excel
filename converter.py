#
# Atlassian Crowd 3.7.0 backup file xml convertor
# processses file and creted two excels needed to import data to another Crowd
#
# 26.4.2022 mika.nokka1@gmail.com


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

for i in range(0,len):
    print ("NUMBER:{0}".format(i))
    #print (data_dict['crowd']['users']['user'][i])
    print (data_dict['crowd']['users']['user'][i]['name'])
    print (data_dict['crowd']['users']['user'][i]['firstName'])
    print (data_dict['crowd']['users']['user'][i]['lastName'])
    print (data_dict['crowd']['users']['user'][i]['email'])
    print (data_dict['crowd']['users']['user'][i]['credential'])
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
    
for i in range(0,counter-1):
    print ("NUMBER:{0}".format(i))
    print (data_dict['crowd']['memberships']['membership'][i]['parentName'])
    print (data_dict['crowd']['memberships']['membership'][i]['childName'])    
    print (".......................................................................")


print ("User found:{0}".format(len))
print ("Directory memberships found:{0}".format(counter))


workbook1.close()
workbook2.close()