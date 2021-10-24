import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(100))
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = (String(250))

class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    user_to_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    user_from_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    user = relationship("User")

    def to_dict(self):
        return {
        "user_to_id":self.user_to_id,
        "user_from_id":self.user_from_id
        }

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    user = relationship("User")

    def to_dict(self):
        return {
        "user_id":self.user_to_id,
        }

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(256), nullable=False)
    author_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    user = relationship("User")
    post_id = Column(Integer, ForeignKey('post.id'), primary_key=True)
    post = relationship("Post")

    def to_dict(self):
        return {
        "id":self.id,
        "comment_text":self.comment_text,
        "author_id":self.author_id,
        "post_id":self.post_id
        }
        
class TypeEnum(enum.Enum):
    image=1
    icon=2
    text=3

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    type= Column(Enum(TypeEnum))
    url= Column(String(50))
    post_id = Column(Integer, ForeignKey('post.id'), primary_key=True)
    post = relationship("Post")

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e