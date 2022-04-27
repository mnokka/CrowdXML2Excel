#
# TODO DESC
#
# 26.4.2022 mika.nokka1@gmail.com


import json
import xmltodict

#hardcocde Atlassian Crowd 3.7.0 backup xml filename 
with open("backup.xml") as xml_file:
     
    data_dict = xmltodict.parse(xml_file.read())
    xml_file.close()
     
for key,val in data_dict.items():
    for val in data_dict[key]:
        print ("key: {0}  value: {1}".format(key,val))
        print ("----------------------------------------------------")

# len works 
len=(len(data_dict['crowd']['users']['user']))

for i in range(0,len):
    print ("NUMBER:{0}".format(i))
    #print (data_dict['crowd']['users']['user'][i])
    print (data_dict['crowd']['users']['user'][i]['name'])
    print (data_dict['crowd']['users']['user'][i]['firstName'])
    print (data_dict['crowd']['users']['user'][i]['lastName'])
    print (data_dict['crowd']['users']['user'][i]['email'])
    print (data_dict['crowd']['users']['user'][i]['credential'])
    print (".....................................................................")
    


counter=0 #len did not work with membership subdictionary
for i in data_dict['crowd']['memberships']['membership']:
    #print (i)
    counter = counter+1
    #print ("----------------------------")
#print (counter)    


for i in range(0,counter-1):
    print ("NUMBER:{0}".format(i))
    print (data_dict['crowd']['memberships']['membership'][i]['parentName'])
    print (data_dict['crowd']['memberships']['membership'][i]['childName'])    
    print (".................")



