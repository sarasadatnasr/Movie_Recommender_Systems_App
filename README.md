# Movies_Recommender_System_App
Movie recommendation systems are an integral part of the entertainment industry, aiming to provide personalized movie suggestions to users based on their preferences. The project entails analyzing a large dataset of movies, incorporating user preferences, and implementing algorithms to generate relevant movie recommendations.

![alt text](Media/recommender.png)

The goal of recommender systems is to offer users customized recommendations of items that match their needs.
There are three main approaches to designing and implementing recommender systems: collaborative filtering, content-based filtering, and hybrid filtering.

• Collaborative filtering leverages the feedback of a group of users to generate recommendations for a target user. The main assumption behind
Collaborative filtering is that users who have similar preferences in the past will also have similar preferences in the future. Collaborative filtering can
be further divided into two subtypes: memory-based and model-based.
– Memory-based Collaborative filtering uses similarity measures to compute recommendations based on the rating matrix, such as k-nearest
neighbors (kNN) or cluster-based approaches.
– Model-based Collaborative filtering uses machine learning algorithms to learn a latent representation of users and items from the rating matrix, such as matrix factorization, singular value decomposition, or neural networks.

• Content-based filtering relies on the features of the items to generate recommendations for a target user. The main assumption behind Content-based filtering is that users will like items that are similar to the ones they have liked in the past. Content-based filtering can also use machine learning algorithms to learn a user profile that captures the user’s preferences based on their feedback history.

• Hybrid filtering combines Collaborative filtering and Content-based filtering. Examples include Factorization Machines and Graph-based approaches.
It is important to note that a family of algorithms can have members in multiple approaches. For instance, only clustering the items based on their features can be considered a content-based approach, meanwhile clustering the users can be considered a collaborative filtering approach.
In this report, we implement multiple recommendation systems and evaluate them on The Movies Dataset. The Movies Dataset is a collection of data on 45,000 movies and contains information such as budget, revenue, release dates, languages, production countries, and companies for each film. The dataset also includes ratings of 270,000 users for these movies. This dataset consists of multiple .csv files describing the movies and the ratings the users gave them. We detail how we cleaned, integrated, and preprocessed the data in subsection

![](Media/recommender.gif)
