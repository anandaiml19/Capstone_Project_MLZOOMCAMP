# Capstone_Project_MLZOOMCAMP
<h1 align="center"> Mango Fruit Disease Classifier

  
### __About Project👨‍💻__ 

•The project deals with the development of a disease classifier CNN model for the Mango fruit. Mango is a national fruit of india,pakisthan and philippines.
Mango trees grown to 30-40 m tall and have a crown radius of 10-15m (source:wikipedia). The raw mango fruit is often attached by many diseases.
Some of the most common diseases in mangos are Anthracnose, Alternaria, Black Mould and Stem and Rot.
Often Farmers find it difficult to identity the type of disease ehich attacked the mangoes. 
The model developed from this project can serve as tool for the farmers to identify the type of disease on the mangoes.

The model developed from this project can also be used to isolate the healthy and diseased mangoes that in turn may be helpful for the final packing of good mangos.
A total of images belonging to five different classes viz., Anthracnose, Alternaria, Black Mould,Stem and Rot and healthy were used for this project. 

<p  align="center"><img width="50%" src="https://github.com/anandaiml19/Capstone_Project_MLZOOMCAMP/blob/main/im1.png" /></a></p>

### __Image Preprocessing and Sizing – Exploratory Image Analysis__ 
<p  align="center"><img width="70%" src="https://github.com/anandaiml19/Capstone_Project_MLZOOMCAMP/blob/main/im2.png" /></a></p>

### Image Train-Validation-Test Split
<p  align="center"><img width="70%" src="https://github.com/anandaiml19/Capstone_Project_MLZOOMCAMP/blob/main/OT1.jpg" /></a></p>

### CNN Model parameters and Tuning
<p  align="center"><img width="70%" src="https://github.com/anandaiml19/Capstone_Project_MLZOOMCAMP/blob/main/OT2.jpg" /></a></p>
 
 ### Model Evaluation and Test Image Prediction
<p  align="center"><img width="50%" src="https://github.com/anandaiml19/Capstone_Project_MLZOOMCAMP/blob/main/im3.png" /></a></p>

***Web Service – Flask ,Html and Docker (Testing the final model with new images)***

### New Imaages predicted by the Final CNN model
<p  align="center"><img width="50%" src="https://github.com/anandaiml19/Capstone_Project_MLZOOMCAMP/blob/main/OT3.jpg" /></a></p>
<p  align="center"><img width="50%" src="https://github.com/anandaiml19/Capstone_Project_MLZOOMCAMP/blob/main/OT5.jpg" /></a></p>
<p  align="center"><img width="50%" src="https://github.com/anandaiml19/Capstone_Project_MLZOOMCAMP/blob/main/OT6.jpg" /></a></p>
<p  align="center"><img width="50%" src="https://github.com/anandaiml19/Capstone_Project_MLZOOMCAMP/blob/main/OT8.jpg" /></a></p>
<p  align="center"><img width="50%" src="https://github.com/anandaiml19/Capstone_Project_MLZOOMCAMP/blob/main/OT9.jpg" /></a></p>

***Steps Involved in deployment in Azure***


1. Create a new container registry in Azure services with a new resource group and
    registry name.
2. Save the container registry name and password in a separate file for future
    reference.
3. Upload all the required project file (app.py,requiremts.txt, template folder with 
    html file, static folder for image storage) in to a new github repository.
4. Build a docker image with a tag name using all project files in folder.
5. Log in to the container registry with the username and password. Once authenti-
    cated, push the docker image in to the container registry.
6. Create a web app service for container registry in Azure services, and choose the 
    docker image previously uplaoded in the container registry.
7. Move in to the deployment center in the created web app service, and choose
    to use github actions for deployment.
8. Move in to your github account account and check for .git file written in the 
    github folder structure.
9. Move in the Actions menu of the Git hub services and wait the processes to 
    complete.
10. Move in to web app service menu and look for the deployed url of the web 
     app service.
11. Now the Mango fruit disease app can be accessed using the devloped web url.


 



### Liked my Contributions:question:[Follow Me](https://github.com/anandaiml19):point_right: [Nominate Me for GitHub Stars](https://stars.github.com/nominate/) :star: :sparkles:
##For any doubts/queries 🔗 👇
                                                                                                                            
<p align="left"> <a href="https://twitter.com/drkrishnaanand_/" target="blank"><img src="https://img.shields.io/twitter/follow/Dr.krishnaanand_?logo=twitter&style=for-the-badge" alt="Drkrishnaanand_" /></a> </p>
<a href="https://www.linkedin.com/in/drkrishnaanand" target="blank"><img align="center" src="https://img.shields.io/badge/-drkrishnaanand-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://in.linkedin.com/in/dr-krishna-anand-v-g-70bba623/" alt="drkrishnanand" height="20" width="100" /></a>
<a href="https://github.com/anandaiml19 /" target="blank"><img align="center" src="https://img.shields.io/github/followers/anandaiml19?label=Follow&style=social&link=https://github.com/anandaiml19 /" alt="drkrishnaanand " height="20" width="90" /></a>
