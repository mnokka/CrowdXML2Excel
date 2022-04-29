# CrowdXML2Excel


Atlassian Crowd 3.7.0 backup file xml to excels convertor.<br>
Processses the backup file and creates two excels needed to import data to another Crowd<br>
(Crowd 3.7.0 seems to have bug not be able to import normal XML backup file)<br>
<br>
<br>
 This script generates two excels; user and group ones. Save them as "csv" (comma delimetered)<br>
 Save also "empty" users csv file (just with titles, no user info at all)<br>
<br>
 In Crowd User import section:<br>
 Phase 1: Import users and groups csv files (creates users and groups)<br>
 Phase 2: Import Empty users and (normal) groups files (adds users to their groups)<br>
<br>
<br>
Seems that creation of csv files (saving as) worked only (Crowd to accept files) when done in Linux using LibreOffice 


