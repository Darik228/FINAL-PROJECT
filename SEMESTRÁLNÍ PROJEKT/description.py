#  Description of models and relationships between them

"""
1. The Author model
A model containing objects of all authors.
It has the following fields:
1) one-to-one relationship with the built-in user model;
2) user rating. Below is a description of how this rating can be calculated.
2. Category Model
Categories of news/articles — the topics they reflect (sports, politics, education, etc.). Has a single field: the name of the category. The field must be unique (the unique = True parameter must be written in the field definition).
3. Post Model
This model should contain articles and news that users create. Each object can have one or more categories.
Accordingly, the model should include the following fields:
1) one-to-many relationship with the Author model;
2) a field with a choice — "article" or "news";
3) automatically added creation date and time;
4) the many-to-many relationship with the Category model (with an additional PostCategory model);
5) the heading of article/news;
6) the text of the article/news;
7) rating of the article/news.
4. PostCategory model
An intermediate model for many-to-many relationship:
1) one-to-many relationship with the Post model;
2) one-to-many relationship with the Category model.
5. Comment Model
You can leave comments under each news/article, so you need to organize their storage method too.
The model will have the following fields:
1) one-to-many relationship with the Post model;
2) one-to-many relationship with the built-in User model (any user can leave comments, not necessarily the author);
3) comment text;
4) date and time the comment was created;
5) comment rating.
"""

#  These models should also implement methods:
"""
1. Like() and dislike() methods in the Comment and Post models, which increase/decrease the rating by one.
2. The preview() method of the Post model, which returns the beginning of the publication (preview) 
with a length of 124 characters and adds an ellipsis at the end.
3. The update_rating() method of the Author model, which updates the user rating passed to the argument of this method.
It consists of the following:
1) the total rating of each author's article is multiplied by 3;
2) the total rating of all the author's comments;
3) the total rating of all comments to the articles; the author.
"""

#  Queries (all commands are in the commands file)
"""
1. Create two users.
2. Create two objects of the Author model associated with users.
3. Add 4 categories to the Category model.
4. Add 2 articles and 1 news item.
5. Assign categories to them (at least one article/news should have at least 2 categories).
6. Create at least 4 comments to different objects of the Post model (each object must have at least one comment).
7. By applying the like() and dislike() functions to articles/news and comments, adjust the ratings of these objects.
8. Update users ratings.
9. Output username and the rating of the best user.
10. Display the date of addition, username of the author, rating, title and preview of the best article, based on likes/dislikes to this article.
11.Display all comments (date, user, rating, text) to this article.
"""
