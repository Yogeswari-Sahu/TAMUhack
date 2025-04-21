# TAMUhack
# MediCo
## Inspiration

With the increase in the internet usage and cheaper data, much of the world is now online. This has a great impact on the health industry as people are searching online for cure and symptoms of diseases and also diagnosing themselves. Many cases of false diagnostics and cure have resulted in fatal injuries or adverse effects. If there is important information needed it is hidden behind a paywall and not easily accessible. In some cases drugs are not provided with their side effects and the patient has to go online to search them. Many of these people are new users in the world wide web.

With Medico we intend to create a platform which provides all important information in one place. Our chatbots are designed to give the user a seamless experience by providing concise information about the query. We believe no information should be hidden or tough to find. We have gathered all data needed by a patient in one place. 
As Anne Wilson Scdhaef has said, “Good health is not something we can buy. However, it can be an extremely valuable savings account.” We wish to light a beacon of hope in these tough times. No person should haggle to get important and necessary information. We all know how much pain in the neck finding the right information online is. With our platform we want to give it a new lease of life.


## What it does
When we search for something specific, let it be a disease or a particular medicine it takes us a lot of time to go through various sites and that is the challenge, our project addresses. We are providing a User friendly Interface to get access to all kinds of data a user would require at one single place, be it any general query or be it about any specific medicine or if the user wants to know about any symptoms of an illness.  
 
## How We built it
First we searched for the appropriate data from various sites that we wanted the users to access and retrieved it by Web Scraping using various python libraries such as BeautifulSoup, lxml, html5lib and requests . After that, we processed the data retrieved using various libraries such as numpy, pandas and many more NLP libraries under the NLP tool, Natural Language Toolkit (NLTK). We trained the data using the TF-IDF model. In this model, the Term Frequencies (or, TF) is calculated for each word. TF is defined as the ratio between the numbers of repetitions of a word in a sentence to the total number of words in a sentence. Then Inverse Document Frequency (or, IDF) is calculated for each word. IDF is defined as the logarithm of the ratio of number of sentences to the number of sentences that contain the particular word. Now, the TF and IDF values for each word in each sentence are multiplied. This gives us the vectors for each word with respect to each sentence, which are treated as the output vectors, or our dependent feature. We then used this model to answer the user’s queries by making Chatbots in our User Interface.

## Challenges We ran into
We went through various challenges. Data plays a major role in the digital world. In our project, we faced a major issue to search for the right kind of data and scraping it in an appropriate form. The next challenge we faced was in training and preprocessing of the data and making it available in a user friendly manner. The toughest challenge we ran into was integrating our model with the User Interface. After gaining all the necessary knowledge we were able to overcome the challenges we faced. 

## Accomplishments that I'm proud of
The data which we were able to gather gives a concise information about general health, diseases and drugs. We were able to provide a seamless user experience with appropriate information. The portal has been designed keeping in mind to provide accessibility to all. The User Interface has been integrated with a machine learning model which lays out a coherent interface for the users.

## What I learned
We learnt how to make a question answering model after data processing using various NLP (Natural Language Processing ) techniques. In the same process, We learnt about how NLP plays a big role in today’s technology. Natural Language Processing(NLP), a field of AI, aims to understand the semantics and connotations of natural human languages. It focuses on extracting meaningful information from text and training data models based on the acquired insights. We learnt about the various libraries in the flask framework and under the Natural Language Toolkit. Moreover we also learnt about the pretrained Machine learning model TF-IDF and making a chatbot with the trained data.

## What's next for MediCo?
In the future, we plan to make this into an Android and an IOS Application. We also plan to add additional features like, diagnosing based upon various symptoms and if needed, a geolocation for nearly hospitals.

## [Demo video Link](https://www.youtube.com/watch?v=5cBWJox9sCE&t=9s)

## Our Collaborators
[Saksham Madan](https://github.com/Hawk453)
[Yogeswari Sahu](https://github.com/Yogeswari-Sahu)
[Akshat Gupta](https://github.com/Akshat1903)
[Shubh Gupta](https://github.com/Shubh0405)
