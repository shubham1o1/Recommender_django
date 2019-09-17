## An AI-LESS Article recommender system in Django:

I referenced some sources to develop a recommender system. The math parts of the recommender system were overwhelming (which has encouraged me to learn maths for machine learning even more) and the implementation which I found were not helpful for the production ready system. I had retained less than 10% out of what I researched and out of those 10% I may have used merely 1-2 % of knowledge to build this system. From what I have understood, the cardinal component that a recommender system needs is the basis to establish a relationship between an item to recommend and the user is to be recommended. For example there can be a list of movies in a website such as Netflix and user might click on an action movie. Then we can use that information in the future to recommend other action movies to that user. So, based on this idea of establishing a relation between item and user, I decided to develop a simple recommender where the basis of commonality is the category of the item.

I have developed this as an initial phase recommender system. This works way worse than other recommender system available on the market. The basic idea that this recommender system uses is this - it collects the user preference when a user clicks on the article's link. And accordingly shows those article that fall under the category that he/she had browsed previously. So for example, if a user clicks on a link that is of "National" category then under **Recommended section:** our system shows article from the list of article that falls under the "National" category. The category of an article is pre-determined when uploading an article.

I have added the feature of login, sign up, log out because we need a user who we recommend an article to. The article/item is recommended according to the user. There is no recommendation if the user is not logged in. It is basically a small work on recommender's architecture and relatively more efforts were put on the django's part. My front end presentation sucks and the data structure to store the user's preferences in the database is also not satisfactory. As I mentioned earlier, this system can be seen as a starting phase of the system to improve upon in the future. There are not limit set on the number of articles to display as recommended article or as the general article, neither are there any pagination added to the page. 

___

### The core architecture of the system:

- Users and article have one thing in common, which is the category. This is the key parameter we use to establish the relationship between the user and the article.
- Category classifies the article and expresses the user's preference.
- I have made a dictionary that holds *username*, *key* that is category of the article that user has read and the *value* that keeps the count of the number of times user read that category. If a user **"John"** has previously clicked on the article that was of **"National"** category **2** times then our datbase will have a data dictionary saved as **"John","National",2**.
- So, we basically have to in this list of dictionaries in the database to find the category and the weightage of that category for the logged user. 
- Our system should save every new category of article he/she has read.
- Our system should also update the count if she/he reads the news of category that is already saved.
- Based on the retrieved information of the user we must recommend the news to the user. 
