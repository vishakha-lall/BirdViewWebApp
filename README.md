## Purpose

To provide an interactive platform where bird watchers can identify a bird that they spot. 

#### Services:

**Bird Recognition:** The user uploads an image of a bird. The application returns the top 5 matches and relevant data of each bird.

**Locate a Bird (in development stage): **The user queries for a bird. The WebApp returns the location closest to the user where the bird can be found.

**Bird Dictionary:** This returns a list of all birds that the application is capable to identify. Currently the WebApp is trained to identify 200 different species of birds as sourced in the Caltech-UCSD Birds-200-2011 Dataset.

**Discover Birds:** The user queries for a bird. The application returns all relevant data about the bird.

## Technologies used

**Spring Boot:** Spring Web Framework and Spring Boot are used for servlet deployment, dispatcher servlet and web framework with MVC architecture.

**AngularJS:** AngularJS is used for two-way data binding.

**JAVA:** JAVA Dynamic Web Framework is used for Server-Side programming.

**HTML5 CSS Bootstrap:** HTML5, CSS and Bootstrap are used as Front-End technologies.

**Maven:** Apache Maven is used to resolve dependencies.

**Tomcat:** Apache Tomcat server is used fordeployment.

**Tensorflow:** Tensorflow is used to retrain the last layer of inception model which was trained on ImageNet and training it for the 200-class classification problem from the UC SD – Caltech CUB 2011 Extended dataset.

**MediaWiki API:** MediaWiki API is an interface made available by Wikimedia Foundation to access Wikipedia’s Content and metadata in machine/human readable formats and for use by developers.

**Python 2.7.12:** Python 2.7.12 is used fo rServer-Side programming.

**Apache 2.0 Server**: It is a web server software and has interface support for python.

**JSON:** JSON is a light-weight data interchange format, it is structured, easy to transfer, read and store. It is used for exchanging data between servers and server and frontend in the WebApp.

**Caltech-UCSD Birds-200-2011 Dataset:** It is an image dataset with photos of 200 bird species. Authored by: Wah, C. andBranson, S. and Welinder, P. and Perona, P. and Belongie, S.

## Flowcharts
![image](https://user-images.githubusercontent.com/31643223/37350741-9499e2e8-26ff-11e8-808c-aad5e33554ce.png)
![image](https://user-images.githubusercontent.com/31643223/37350777-a28d496c-26ff-11e8-8aec-fa468e5831e8.png)
![image](https://user-images.githubusercontent.com/31643223/37350788-a8852da8-26ff-11e8-958f-693786ada0be.png)
##  Folder Structure
![image](https://user-images.githubusercontent.com/31643223/37350815-b80a2f58-26ff-11e8-8af1-9277b81eed68.png)
## Server-side functions and scripts

**WebInitializer.java**

- Configures Spring Boot Application
- Initialize Storage Service

 **MainController.java**

- Initializes users 

**LoginController.java**

- Authenticates credentials

**SignUpController.java**

- Adds a new user

**UploadController.java**

- Stores uploaded image to directory on server

**ResultController.java**

- Captures JSON object from server 2 and returns to front-end controllers

**app.js,appConfig.js, appController.js**

- Configure angular controllers
- Configure $location
- Configure $service

**loginController.js**

**signupController.js**

**nouserController.js**

**homeController.js**

**uploadController.js**

**discoverController.js**

**dictionaryController.js**

**resultController.js**

**resultDiscoverController.js**

**imageOpener.py**

- Responds to POST requests which upload a jpeg file.
- Uses CGI
- Extracts payload from the request
- Assigns a token to the request.
- Updates the token count.
- Stores the image with this token id.
- Calls mastercontroller.py
- Converts the returned objects into a JSON object.
- Returns the response as JSON object.

**mastercontroller.py**

- Gets data from other utility scripts, coordinates among them and returns the result to imageOpener.py
- Calls masterlabeller.py to get the top 5 labels.
- Passes these labels iteratively tomasterextractor.py
- Gets summary, Wikipedia links, location brief, linkto images from masterextractor.py
- Returns everything to the caller.

**maslabeller.py**

- Receives the path to the image to be labelled. Returns the list of top 5 bird species matching the image.
- Reads the image file as binary
- Reads the output labels file
- Loads the trained model
-  Obtains a Tensorflow session
- Uses Softmax in the last layer to assign scores toimages in the range [0,1].
- Sorts them by score in descending order
- Returns top 5 scoring species labels

**masterextractor.py**

- Receives label/species name. Returns summary,Wikipedia links, location brief, link to images.
- Runs a search on Wikipedia database using mediaWIKI API.
- Gets metadata viz. page id, page title, etc.
- Gets extract, Wikipedia page link.
- Uses wptools package utilities to get imagelinks from infobox from wikipage.
- Gets raw link to the images using mediaWIKI API.

 **masterlocationextractor.py**

- Receives the wiki page id. Returns a brief on locations where the bird is found.
- Uses string processing and parsing to extractlocation information from the wikipedia page about the bird.
- Returns the relevant data.



## Screenshots
![image](https://user-images.githubusercontent.com/31643223/37350855-ca92a9fc-26ff-11e8-95e4-7de390cb35cb.png)
![image](https://user-images.githubusercontent.com/31643223/37350861-ce6b7c2a-26ff-11e8-8df4-7e947d047423.png)
![image](https://user-images.githubusercontent.com/31643223/37350870-d15c6296-26ff-11e8-8c91-f7ddd051755c.png)
![image](https://user-images.githubusercontent.com/31643223/37350873-d368b602-26ff-11e8-8f9f-84fbcb29a53a.png)
![image](https://user-images.githubusercontent.com/31643223/37350877-d6322fda-26ff-11e8-8c49-4af866221d1a.png)
![image](https://user-images.githubusercontent.com/31643223/37350883-d9393fac-26ff-11e8-9f21-005406b4f4ff.png)
![image](https://user-images.githubusercontent.com/31643223/37350891-dc05dca4-26ff-11e8-99d9-ed0d44c3ce38.png)
![image](https://user-images.githubusercontent.com/31643223/37350895-de774bbc-26ff-11e8-93de-9e9d27ce2d91.png)
![image](https://user-images.githubusercontent.com/31643223/37350900-e15cac64-26ff-11e8-8db7-f21a94d645e9.png)
![image](https://user-images.githubusercontent.com/31643223/37350901-e366418c-26ff-11e8-8c24-8ecba55ee0c3.png)
![image](https://user-images.githubusercontent.com/31643223/37350904-e602c92e-26ff-11e8-809e-d6a29777ce7c.png)
![image](https://user-images.githubusercontent.com/31643223/37350909-e85b2126-26ff-11e8-8068-2366d54f8c6c.png)
![image](https://user-images.githubusercontent.com/31643223/37350914-eae9546c-26ff-11e8-8540-bdcc511ba5bb.png)
![image](https://user-images.githubusercontent.com/31643223/37350921-ed77eb80-26ff-11e8-97d9-360ceec9fc37.png)
![image](https://user-images.githubusercontent.com/31643223/37350923-f0516958-26ff-11e8-8b36-ecd7c6803da7.png)
![image](https://user-images.githubusercontent.com/31643223/37350924-f2aef652-26ff-11e8-99c6-4609df4c084e.png)
![image](https://user-images.githubusercontent.com/31643223/37350928-f509ff3c-26ff-11e8-8411-20396884bf2a.png)
![image](https://user-images.githubusercontent.com/31643223/37350940-f7e88688-26ff-11e8-9c0c-3dde8db16ba4.png)
![image](https://user-images.githubusercontent.com/31643223/37350946-fb65c140-26ff-11e8-9331-e1b4b8bb8dfa.png)
![image](https://user-images.githubusercontent.com/31643223/37350951-fd2fce8a-26ff-11e8-8b32-43dc62f8f1ca.png)
![image](https://user-images.githubusercontent.com/31643223/37350961-013e7a08-2700-11e8-9e69-a5f71ec0a42d.png)

## Areas of further development

- Data fetched from Wikipedia can be stored in a database and this database can be periodically updated.
-  Additional content can be either manually added or extracted from other internet sources.
- CGI can be replaced with WSGI or a multithreaded request handler which will create light weight instances of the imageOpener.py script.
- GoogleMaps API can be used to display locations where birds are found after extracting location entities using Named Entity Recognition from parsed location information.
- Currently we are classifying 200 species, the number of species can be extended.
- An extensive database can be developed to keep track of users and their activities.
- Training and labelling can be further improved by exploring techniques like image segmentation followed by classification.
- Additional miscellaneous service can be added.
