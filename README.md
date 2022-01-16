# BD_AGRO_D-JANGO_SYSTEM
BD AGRO DJANGO PROJECT.

https://github.com/SAZZAD-AMT/BD_AGRO_D-JANGO_SYSTEM/blob/main/static-files/BDAGRO_(2018-3-60-018)_(2019-1-60-063)_(2018-2-60-068).pdf

https://github.com/SAZZAD-AMT/BD_AGRO_D-JANGO_SYSTEM/blob/main/static-files/270238369_1089022861847212_3024622906751422312_n.jpg?raw=true

from django.db import models
from django.db.models.deletion import CASCADE
import uuid
from user.models import User


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    tags = models.ManyToManyField("Tag", blank=True)
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )

    def __str__(self):
        return self.title


class Review(models.Model):
    VOTE_TYPE = (
        ("up", "Up Vote"),
        ("down", "Down Vote"),
    )
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )

    def __str__(self):
        return self.value


class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )

    def __str__(self):
        return self.name
        
        
     East West University
Department of CSE
Project Title: BD AGRO System
Course code: CSE347(2)
Semester: FALL 2021
Group Member Information:
Name: Khaledur Rahman
ID: 2018-3-60-018
Name: Asef Amer
ID:2018-2-60-068
  Name: Sazzad Hossen
ID:2019-1-60-063
		
Submitted to:
Md Mohsin Uddin
Senior Lecturer
Department of Computer Science and Engineering
East West University



TABLE OF CONTENTS

Topic	                                                                                                                page					   		                        	           		          

Introduction & Motivations ………………………………………………… 3
Challenges …………………………………………………………………  4-5
Requirements ……………………………………………………………….4- 7
	Non-functional Requirements ……………………………………………5 
	Functional Requirements ……………………………………………….. 5-6
Technologies ……………………………………………………………………..6
UML Use Case Diagram------------------------------------------------------------------7
UML Class Diagram-----------------------------------------------------------------------8
Activity Diagram----------------------------------------------------------------------------9
Sequence Diagram--------------------------------------------------------------------------10
ER diagram-------------------------------------------------------------------------------------------11
GUI-----------------------------------------------------------------------------------------------------(12-34)









Introduction
BD Agro System is a service and information providing platform that makes life easy and saves time for the farmers who wants to acquire information regarding their crops especially, in terms of insecticides and which weather is suitable for creating a particular crop in a specific pH of land. Moreover, in case of emergency, clients can take advice from prominent experts and also Search for a specific item or list. Furthermore, they can also order fertilizers and insecticides at the cheapest price. This document contains the software requirements specification (SRS) for said app.

Motivations
•	The main goal of our app is to give people the opportunity to get services by seeking information through an app. For example-if one needs to know which insecticides will assists them in growing a specific crop, then they’ll have to go to the website and ask experts or go through the saved information’s by using search option. 
•	Our app is targeted to make life easier for people by providing service. For example-In this pandemic, people are at remote areas cannot move freely so if they need to buy fertilizer they can’t go to market because of safety issues. So, in this situation they can order through website and get the required substance.
•	Through this app clients can give review after taking service and recommend for future. All of that information available will be constantly available through the app’s intuitive UI. 
Challenges
•	Implementing certain features such as searching and ordering in a web-application.

•	Since this project is entirely team driven, we lack any client or upper-management feedback. Lacking well-defined client-requirements will make the development process a little more difficult.

•	Adding to the previous point, since we lack any client-defined deadlines, proper time management will also be an issue. To remedy this, the team as decided to use the Agile Scrum development method.

•	Integrating several APIs into the application and ensuring they work properly together.

•	Getting the team familiar with technologies they haven’t worked with before, namely, Django and Python.

•	Making sure the UI isn’t too technical or cluttered and follows the latest design trends.

•	Not being able to test the responsiveness of the app in certain devices/platforms the team doesn’t have access to, such as Safari browser (iOS), smart-televisions, etc. 


•	Internet Explorer probably won’t be able to support many of the app’s features. However, since IE isn’t very popular with the targeted audience, this should be considered a minor hindrance at best.

•	Ensuring strict client security and protecting the client’s data.

Non-functional Requirements
For BD AGRO system types of non-functional requirement 
1.	Safety / security Requirement.
2.	Environmental Requirement.
3.	Usability Requirement.
4.	Performance Requirement.
5.	Development Requirement.

Functional Requirements 
In BD AGRO system need a functional requirement 
1.	A user can easily access recommended option following the flow chart.
2.	BD AGRO is very user-friendly application. User can see all the current option in the menu bar.
3.	While using BD AGRO user can get First help, quick replies and solutions.

4.	User can see he/her profile, Number, Address, Location Including log out, log in option.
5.	User can Order Fertilizer and other agricultural tools from BD AGRO Application. The package will be delivered to the users in the correct location in 2/3 business day.
6.	BD AGRO also give you the suitable season and weather details for cultivating crops.
7.	BD AGRO gives the best advice to the user by our expert doctors online. Just click the photo of the crop disease then upload the picture and add your location, phone number, our expert doctor will advise the user in the description box what will be the solution or medicine for the disease.
8.	 There will be Agricultural news and Update in the Application so the user can get the updated news of the current situation. 
User authentication: Since our app deal with sensitive information about the client’s information, a thorough authentication procedure should be followed.
Research Feed: If any fresher and user want to post something about there thesis, research paper or anything what related about agriculture they can post from this section.


Technologies: HTML, CSS, Bootstrap, Database, Python, Django.

 
UML Use Case Diagram:
 
UML Class Diagram:
 
Activity Diagram:
 
 
Sequence Diagram:
 
 
ER diagram:
 

 
GUI of BD AGRO:
BD AGRO Home Page :
 
Login :
 

Sign Up Page :
 
After Login :
 

STATISTIC Page :
 

 


STATISTIC Till 2020 GDP :
 
 

STATISTIC 2021 GDP :
 
 

Profile Of User : 
 
Update Profile :
 



AGRO INFO
Proven Business Strategies is Explained with References 

 
 


 
 


 
 
More Fertilizer Info:
Animated Page Using Hover Effects
 

 
 

 
 

                                                                                Marketing
Create Project 

 
 





Edit the Page
 



Delete the page 






View the Created page
 

WINGS OF AGRICULTURE :

This is our research page , only an Expert Author can post his/her research on this page.Normal user can only view this page. User can not edit or delete any paper from this page.










User View :

 
 




Expert view : 
 


Edit page :
 



Delete page :
 
Farmer's Doctor

Here is the feature where a normal user can post his/her crop problem with His/her Name,Location,Phone number as Discription and post His/her problem there.They can edit and Delete the post they have posted. On the posted Blog An Expert can Give his solution by commenting on the Blog post to let the user know the crops problems 

User view :
 
 
 







Edit  and Update Page:
 


Delete Page :
 



Expert Comments :
 
 

Agriculture News 

Here is the news part of our aplication where users and expert can view news about agriculture from all round the world.No user or Expert can edit any news from this page only admin can post news here and edit and delete post.

 view:
 
 






admin page:
 

edit and delete :
 

