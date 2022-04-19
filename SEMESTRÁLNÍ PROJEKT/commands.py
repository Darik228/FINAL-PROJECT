"""
user1 = User.objects.create_user(username='Peter')
user2 = User.objects.create_user(username='John')
author1 = Author.objects.create(user=user1)
author2 = Author.objects.create(user=user2)
IT = Category.objects.create(category_name='IT')
SPORT = Category.objects.create(category_name='SPORT')
MUSIC = Category.objects.create(category_name='MUSIC')
SCIENCE = Category.objects.create(category_name='SCIENCE')
article1 = Post.objects.create(publication=Post.article, heading='Sports song', text='A sports song was played all over the world today!', rating=3.0, author = author1)
article2 = Post.objects.create(publication=Post.article, heading='Research in the field of IT', text='The grandiose research of scientists in the field of IT shocked the whole world.', rating=4.0, author = author2)
news = Post.objects.create(publication=Post.news, heading='Exhibition of Musical Instruments', text='An exhibition of musical instruments was held at the Museum of Science', rating=2.5, author=author1)
PostCategory.objects.create(post=article1,category=Category.objects.get(category_name='MUSIC'))
PostCategory.objects.create(post=article1,category=Category.objects.get(category_name='SPORT'))
PostCategory.objects.create(post=article2, category=Category.objects.get(category_name='IT'))
PostCategory.objects.create(post=article2, category=Category.objects.get(category_name='SCIENCE'))
PostCategory.objects.create(post=news, category=Category.objects.get(category_name='SCIENCE'))
PostCategory.objects.create(post=news, category=Category.objects.get(category_name='MUSIC'))
comment1 = Comment.objects.create(text='Good', rating=4.0, post=article1, user=user1)
comment2 = Comment.objects.create(text='Nice', rating=5.0, post=article1, user=user2)
comment3 = Comment.objects.create(text='Greate', rating=3.0, post=article2, user=user1)
comment4 = Comment.objects.create(text='bad', rating=2.0, post=news, user=user1)
article1.dislike()
comment1.like()
comment2.like()
comment3.like()
comment4.dislike()
article2.like()
news.like()
rating_peter = (sum([post.rating*3 for post in Post.objects.filter(author=author1)])+
sum([comment.rating for comment in Comment.objects.filter(user=user1)])+
sum([comment.rating for comment in Comment.objects.filter(post__author=author1)]))
rating_john = (sum([post.rating*3 for post in Post.objects.filter(author=author2)])+
sum([comment.rating for comment in Comment.objects.filter(user=user2)])+
sum([comment.rating for comment in Comment.objects.filter(post__author=author2)]))
author1.update_rating(rating_peter)
author2.update_rating(rating_john)
best_author = Author.objects.all().order_by('-rating')[0]
print(best_author.user.username)
print(best_author.rating)
best_article = Post.objects.filter(publication = Post.article).order_by('-rating')[0]
print(best_article.date_of_creation)
print(best_article.author.user.username)
print(best_article.rating)
print(best_article.heading)
best_article.preview()
for comment in Comment.objects.filter(post=best_article):
...     print(comment.date)
...     print(comment.user.username)
...     print(comment.rating)
...     print(comment.text)


"""
