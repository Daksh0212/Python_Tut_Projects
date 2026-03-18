import requests

str1=r"""IITK
G20 
 
Azadi 

Search
English
हिन्दी
Main navigation
Home
Academics
Research
Incubation
People
Administration
Services
Connect
Home
Faculty
Aditya Vikram
Aditya Vikram
Aditya Vikram Ph.D in Quantitative Economics, Indian Statistical Institute, Delhi
Assistant Professor, Department of Economic Sciences

Research Interest
Mechanism design, auction theory

vikrama@iitk.ac.in

0512-259-2311 (O)

https://sites.google.com/site/88avikram

Room 426, ESB-2
IIT Kanpur-208016, Uttar Pradesh, India

Download CV
Basic Information
Research Interest
Contact Information
Education
Teaching Area
Selected Publications
Education
PhD in Quantitative Economics, Indian Statistical Institute, Delhi, 2022

MA in Economics, Delhi School of Economics, 2014
 

MBA, Faculty of Management Studies, 2012
 

BTech in Electrical Engineering (Power), Indian Institute of Technology Delhi, 2009

Teaching Area
Mechanism design, auction theory, matching, market design

Selected Publications
Vikram, A., A top-only mechanism with reserve price for single-good allocation problem. Economics Letters, Vol 217, 2022

About Us
Institute
Academics
NIRF
Consulting
Innovation & Incubation
Campus Life
Contact
Media Coverage
Press Releases
Campus Information
Annual Reports
Animal Welfare Cell
Campus Directory
Internal Complaints Committee
International Relations
Plan Your Visit
Quick Links
Login
Right to Information Act
Tenders
Vigilance
Intranet
Public Grievance
In Memoriam
IITK
Indian Institute of Technology Kanpur
Kalyanpur, Kanpur -208 016

Contact Number:
0512 - 259 - 0151

Emergency Numbers:

Security : 0512 - 259 - 7999, 7994
Police: 0512 - 259 - 7309
Health Center: 0512 - 259 - 7777
Fire Station: 0512 - 221 - 8999
© 2026 Indian Institute of Technology Kanpur

A- A A+ Accessibility
English
हिन्दी

jkfhsj@gmail.ac.in
hello@why.you.are.here


"""

x=str(input("Just throw the Content and we'll filter all the emails for you: (leave blank for dummy)\n"))
if(len(x)>0):
    str1=x


# Using Normal Logic without any RegEx (Regular Expressions)

# all=str1.split()
# emails=[]

# for items in all:
#     j=0
#     k=0
#     countat=0
#     for i in range(len(items)):
#         if(items[i]=="@"):
#             j=i
#             countat+=1
#         if(items[i]=="."):
#             k=i
    
#     if(countat==1 and k-j>0 and j>0 and k>0):
#         emails.append(items)
# i=1
# for items in emails:
#     print("Email " + str(i) + " = " + items) 
#     i+=1



# Using Regular Expressions
import re

relist = re.findall(r"[0-9a-zA-Z.-_%]+@[0-9a-zA-Z.-_%]+[.][0-9a-zA-Z.-_%]+", str1)
print(relist)
i=1
for items in relist:
    print("Email " + str(i) + " : " + items)
    i+=1