# original xml to json example: https://www.geeksforgeeks.org/python-xml-to-json/?ref=lbp


# Program to convert an xml
# file to json file
 
# import json module and xmltodict
# module provided by python
import json
import xmltodict
 
 
# open the input xml file and read
# data in form of python dictionary
# using xmltodict module
with open("backup.xml") as xml_file:
     
    data_dict = xmltodict.parse(xml_file.read())
    xml_file.close()
     
    # generate the object using json.dumps()
    # corresponding to json data
     
    json_data = json.dumps(data_dict)
     
    # Write the json data to output
    # json file
    #with open("data.json", "w") as json_file:
     #   json_file.write(json_data)
     #   json_file.close()
#print (data_dict)
print ("----------------------------------------------------")
#print (json_data)

print(data_dict.keys())
print ("----------------------------------------------------")


print ("----------------------------------------------------")

for key,val in data_dict.items():
    for val in data_dict[key]:
        print ("key: {0}  value: {1}".format(key,val))
        print ("----------------------------------------------------")

        #for key2,val2 in val.values():
        print (val[1])
        print (val[2]) 
      #print (val[1].items())
       
print ("----------------------------------------------------")
    
print (data_dict['crowd']['users']['user'][0])
print ("------------------------------------------------------------")
#print(data_dict['crowd']['users'][0])
print(data_dict['crowd']['groups']) #.get('name'))

print("-----------------------------------------------------")
#for item in data_dict.items():
#    print (item)
#    print ("------------------------------------------------------------------------")


len=(len(data_dict['crowd']['users']['user']))

for i in range(0,len):
    print ("NUMBER:{0}".format(i))
    print (data_dict['crowd']['users']['user'][i])
    print (data_dict['crowd']['users']['user'][i]['name'])
    print (".....................................................................")
    
    
    
    

