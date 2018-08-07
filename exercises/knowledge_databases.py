from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article(article_name, article_topic, article_rating):
	article_object = Knowledge(
		article_name= article_name,
		article_topic= article_topic,
		article_rating= article_rating,
		
	)
	session.add(article_object)
	session.commit()
add_article("cats","cats", 7)
pass

def query_all_articles():
	pass

def query_article_by_topic():
	pass

def delete_article_by_topic():
	pass

def delete_all_articles():
	pass

def edit_article_rating():
	pass
