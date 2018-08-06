from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Knowledge(Base):
    # Create a table with 4 columns
    # The first column will be the primary key
    # The second column should be a string representing
    # the name of the Wiki article that you're referencing
    # The third column will be a string representing the 
    # topic of the article. The last column will be
    # an integer, representing your rating of the article.
    __tablename__ = 'knowledge'
    article_id = Column(Integer, primary_key=True)
    article_name = Column(String)
    article_topic = Column(String)
    article_rating = Column(Integer)
    def __repr__(self):
        return (
           "article id: {}\n"
           "article name: {}\n"
           "article topic: {}\n"
           "article rating: {}\n").format(
               self.article_id,
               self.article_name,
               self.article_rating,
               self.article_topic)

#x = Knowledge("If you want to learn about" + article_name = "cats", "you should look at the Wikipedia article called" + article_name="cats", "we gave this article a rating of" + article_rating= 9 + "out of 10!")
x = Knowledge("If you want to learn about" + article_name = "cats", "you should look at the Wikipedia article called" + article_name="cats", "we gave this article a rating of" + article_rating= 9 + "out of 10!")
print (x)



