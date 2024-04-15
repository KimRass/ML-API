from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base

BASE = declarative_base()


class DBUser(BASE):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False)
    email_addr = Column(String, nullable=False, unique=True)
    created_at = Column(DateTime, default=datetime.now, nullable=True)

    posts = relationship("DBPost", back_populates="writer")
    comments = relationship("DBComment", back_populates="writer")


class DBPost(BASE):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=True)
    created_at = Column(DateTime, server_default="CURRENT_TIMESTAMP", nullable=True)
    updated_at = Column(
        DateTime,
        server_default="CURRENT_TIMESTAMP",
        onupdate=datetime.now,
        nullable=True,
    )

    writer = relationship("DBUser", back_populates="posts")
    comments = relationship("DBComment", back_populates="post")


class DBComment(BASE):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    post_id = Column(Integer, ForeignKey("posts.id"), nullable=False)
    content = Column(String, nullable=True)
    created_at = Column(DateTime, server_default="CURRENT_TIMESTAMP", nullable=True)
    updated_at = Column(
        DateTime,
        server_default="CURRENT_TIMESTAMP",
        onupdate=datetime.now,
        nullable=True,
    )

    writer = relationship("DBUser", back_populates="comments")
    post = relationship("DBPost", back_populates="comments")
