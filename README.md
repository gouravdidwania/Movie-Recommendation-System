<!-- PROJECT LOGO -->
![20d38e00-6634-11eb-9d1f-6a5232d0f84f](https://user-images.githubusercontent.com/86877457/132905471-3ef27af4-ecc6-44bf-a47c-5ccf2250410c.jpg)
<br />
<p align="center">

  <h3 align="center">Movies Recommendation System</h3>

  <p align="center">
    In this project, I'll have build a English Movies Recommendation system with ML concepts and deployed it using StreamLit library using Heroku. This model recommend shows the top 12 recommendation for the given movie name.
    <br />
  </p>
</p>


**Link ---> [Movie Recommender System](https://movie-recommender-system-0.herokuapp.com/)**


<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#problem-statement">Problem Statement</a>
    </li>
    <li>
	<a href="#data-overview">Data Overview</a>
	<ul>
          <li><a href="#data-attributes">Data Attributes</a></li>
          <li><a href="#data-snapshot">Data Snapshot</a></li>
        </ul>
    </li>
    <li><a href="#implementaion">Implementaion</a>
	<ul>
          <li><a href="#data-preparation">Data Preparation</a></li>
          <li><a href="#creating-a-count-vectorizer">Creating a Count Vectorizer</a></li>
	  <li><a href="#calculating-cosine-similarity">Calculating Cosine Similarity</a></li>
	  <li><a href="#predicting-similar-movies">Predicting Similar Movies</a></li>
	  <li><a href="#model-deployment">Model Deployment</a></li>
        </ul>
    </li>
    <li><a href="#final-thoughts">Final Thoughts</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

At some point each one of us must have wondered where all the recommendations that Netflix, Amazon, Google give us, come from. We often rate products on the internet and all the preferences we express and data we share (explicitly or not), are used by recommender systems to generate, in fact, recommendations. 

Recommender systems usually make use of either or both **collaborative filtering** and **content-based filtering** (also known as the personality-based approach),as well as other systems such as knowledge-based systems. I will use movies as an example (because if I could, I would be watching movies/tv shows all the time), but keep in mind that this type of process can be applied for any kind of product you watch, listen to, buy, and so on.

Recommender systems usually make use of either or both collaborative filtering and content-based filtering (also known as the personality-based approach),as well as other systems such as knowledge-based systems.

**COLLABORATIVE BASED FILTERING**

![1_x8gTiprhLs7zflmEn1UjAQ](https://user-images.githubusercontent.com/86877457/132908414-e273f605-e64f-498b-80fd-f3764cfb5969.png)

**CONTENT BASED FILTERING**

![1_BME1JjIlBEAI9BV5pOO5Mg](https://user-images.githubusercontent.com/86877457/132909067-67d85649-9a5a-468f-a0c0-3c43d92e57a5.png)

**Why Recommendation Systems?**

– They help the user find items of their interest
– Helps the item provider to deliver their items to the right user
  – To identify the most relevant products for each user
  – Showcase personalised content to each user
  – Suggest top offers and discounts to the right user
– Websites can improve user-engagement
– It increases revenues for business through increased consumption

<!-- PROBLEM STATEMENT -->
## Problem Statement

The overall aim of this process is to build a content based model which can recommend movied based on the imput movie choice of user.

Insights from this can be used to develop systems for big multimedia and OTT platform to give a better viewing expeience to the users. 

<!-- DATA OVERVIEW -->
## Data Overview

Source: [TMDB](https://www.kaggle.com/tmdb/tmdb-movie-metadata?select=tmdb_5000_movies.csv)

Data: This data contains movies list of 5000 movies from ['The Movie Database (TMDB)'](https://www.themoviedb.org/), as well as various other information ranging from cast, release date, star cast, crew to budget of movie and even the languages in which it was released.

Thier were two data sets which were combined and used as a one

Downloaded the csv file from Kaggle.

### Data Attributes

There are many columns. Only important ones will be discussed here.

**1. Title:** Text column containing the name of the movies. There's anather column containing the name of movies in other languages.

**2. Genres:** JSON format, list containing movies respective generes profile with its id.

**3. Movie ID:** Numbers which represented the unique IDs of movies with which we can search for movies on TMDB.

**4. Keywords:** String containg the small tags which can represent a movie.

**5. Overview:** Text which basically described the plot of the movie.

**6. Cast:** JSON format, Contained the name of the each and every cast from the movie

**7. Crew:** JSON format, Contained the names, job and designation of each and every crew member.

### Data Snapshot

Let’s look at the data. Movies Dataset:

![image](https://user-images.githubusercontent.com/86877457/132911620-b62712a0-b97e-43e6-a08c-2a3731b4c51b.png)

![image](https://user-images.githubusercontent.com/86877457/132911968-23a6e6d3-8bfa-4c43-8584-12a14d7753d7.png)

Credits Dataset:

![image](https://user-images.githubusercontent.com/86877457/132911706-5b6186e2-3c2d-438a-9772-26b37ebc36cb.png)

![image](https://user-images.githubusercontent.com/86877457/132912016-8693ffe6-323a-457b-b2e7-0ee938b988ed.png)


<!-- IMPLEMANTATION -->
## Implementaion

**Real-world/Business objectives and constraints**

- No low-latency requirement.
- Need to provide a better experience to the viewers.
- Should be robust in nature.

### Data Preparation

**Data Preparation Steps:**

1. Explore Each and Every Column.
2. Deal with the Null Values.
3. Merge the Movie dataset and the Credits dataset.
4. Select the columns we want to process.
5. Jsonify the columns required and select the proper keys for analysis.

Let's have a look at the columns we're sealing with:

![image](https://user-images.githubusercontent.com/86877457/132912420-56415926-d2be-484d-a5b5-f53cdca19dbb.png)

After merging our dataset looked like this:

![image](https://user-images.githubusercontent.com/86877457/132912531-7564f6db-a39b-4356-ae51-decaba963656.png)

**Data Cleaning**

We need to jsonify and extract the respective data such as genres, keywords, cast,etc. For that I built a function:

  ```sh
  import json
  
  def cleaner(element):
    name=element['name']
    return name
    
  for i in range(len(df.genres)):
    genres_list = [cleaner(x) for x in json.loads(df.genres[i])]
    df.genres[i] = genres_list
    
  for i in range(len(df.keywords)):
    keywords_list = [cleaner(x) for x in json.loads(df.keywords[i])]
    df.keywords[i] = keywords_list
    
  def cleaner_director(element):
    if element['job']=='Director':
        name=element['name']
        return name
        
  for i in range(len(df.crew)):
    crew_list = [cleaner_director(x) for x in json.loads(df.crew[i])]
    df.crew[i] = [k for k in crew_list if k!=None]
```

Same was performed on the crew column from which the Director name was extracted as many people prefer watching movies froma specific director. Other data was discarded. After this the data looked like this:

![image](https://user-images.githubusercontent.com/86877457/132913150-7ef7a209-05b5-472b-936d-60856bd1309a.png)

The Genres, Keywords, Actors' name, Directors' name with more than one word were merged into one. This step was performed to remove error while representing a persons' name or keyword. Like James Cameraon should be treated as a whole not two different words.

All this data was merged into one column as a string on which we'll be performing Natural Language Processing.

![image](https://user-images.githubusercontent.com/86877457/132913552-bc3344d3-97e1-4e69-a3a0-28ad59175a96.png)

A new dataframe was created with just the movie name and the combined fetures:

![image](https://user-images.githubusercontent.com/86877457/132913681-ad2afdb5-b1cb-41cf-a14f-a0a57ba2e133.png)

We need to remove punctuations and stop words, also lower the letters. Before doing these, the abbreviations need to be converted to regular words because their meaning could be lost while cleaning. I made this function to filter out all the abbreviations from the entire dataset.

**Data Preparation**

I want to try Bags of Words word embedding method. I don't prefer TF-IDF because they could minimize the weightage for cast, genres etc which occur for many times. 

Before performing word embedding, we need to remove punctuations and stop words, also lower the letters. I created a loop to do this task. After running each string will get cleaned and get rif of stopwords.

  ```sh
  '''Stop Words and Other symbols and punctuation should be removed'''
  for i in range(len(df)):
    df.combined[i]=df.combined[i].lower()
    words=nltk.word_tokenize(df.combined[i])
    words=[re.sub('[^a-zA-Z]'," ",word) for word in words if word not in stopwords.words('english')]
    df.combined[i]=' '.join(words)
  ```
  
### Creating a Count Vectorizer

Machine learning models don’t understand human words, but they know vectors!

We'll be count-vectorizing the combined column to covert the textual data to numeric data so that we can process it further. Below shown is how CountVectorizer() works :

![vectorchart](https://user-images.githubusercontent.com/86877457/132914763-2c424b95-ff7d-436e-9c0c-585df1f9989b.png)

 This Convert a collection of text documents to a matrix of token counts. This implementation produces a sparse representation of the counts using scipy.sparse.csr_matrix which we'll convert to an array.

### Calculating Cosine Similarity

The dot product is important when defining the similarity, as it is directly connected to it. The definition of similarity between two vectors u and v is, in fact, the ratio between their dot product and the product of their magnitudes.

![1_r5ULMbx7ju3_Y4TU1PJIyQ](https://user-images.githubusercontent.com/86877457/132915166-a01e5c11-b8f8-49b4-88fc-450c161513d5.png)

By applying the definition of similarity, this will be in fact equal to 1 if the two vectors are identical, and it will be 0 if the two are orthogonal. In other words, the similarity is a number bounded between 0 and 1 that tells us how much the two vectors are similar. Pretty straightforward!

```sh
count_vect=CountVectorizer(max_features=10000)
vector=count_vect.fit_transform(df.combined).toarray()
similarity_score=cosine_similarity(vector)
print(similarity_score)
```
![image](https://user-images.githubusercontent.com/86877457/132915443-81fa5754-a518-4f02-ab5e-1a6d6e0a4583.png)

### Predicting Similar Movies

A **Best Movie** will be that movie whose cosine similarity score with the given movie will be highest.

I created a fucntion which will compare the cosine similarity score of all the movies with the given movie, sort it in descending order and store it in a dataframe.

  ```sh
  def recommend(movie_user):
    movie_index=df[df.title==movie_user].index.values[0]
    similar_movies=pd.DataFrame(enumerate(similarity_score[movie_index])).drop(0,axis='columns').sort_values(by=1,ascending=False)
    similar_movies['Names']=list(map(lambda x:str(np.squeeze(df[df.index==x['title'].values)),similar_movies.index.values))
    
    similar_movies['id']=list(map(lambda x: int(np.squeeze(df[df.index==x]['id'].values)),similar_movies.index.values))
    
    return similar_movies.Names.values[:10]
 ```
 
This is what the function returns:

![image](https://user-images.githubusercontent.com/86877457/132915986-6c5854d1-e5b0-44a1-a784-ae3868228ecd.png)

### Model Deployment

Deployed the model on local server with the help of Streamlit Library. I must say, it was very efficient to use. Then for finally publishing it online, I took the help of Heroku.

For the top 12 movies it matches the the movie id with the TMDB database and extract other information for the movies from the websites. I chose to display the poster along with names on the site.

Link ---> [Movie Recommender System](https://movie-recommender-system-0.herokuapp.com/)

![image](https://user-images.githubusercontent.com/86877457/132916934-266d1fb7-fa5b-449f-90ea-21811adfe03f.png)

<!-- FINAL THOUGHTS -->
## Final Thoughts

The job is done! Of course this is a pretty limited recommender system because I only used a dataset with 5000 english movies, but it’s not bad at all! Following the same procedure but using more data, and implementing the same methodology, this system can be easily refined. The system was tested for many movies and the results were splendid.

This looks good to me! I can always see high similarities based on genres and plot, mainly. I love the movies in the list above that I already saw, as much as I love Spider-Man, so I guess I’ll go watch the couple of titles I am still missing!

**FURTHER IMPROVEMENT**

- The current analysis is based content type recommendation system. I would like to collect more data and recent data like user ids and user ratings to improve the model.
- We can try implementing multiple movies input which can give user a more specific result.
- With proper data we can try adding Hindi movies as well. This will add even value to the project.
