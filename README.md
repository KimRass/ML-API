# Assignment1

## 사용된 클라우드 플랫폼과 인스턴스 구성에 대한 설명

## 선택한 API 프레임워크의 장단점 및 사용 이유에 대한 설명
- Pydantic: 데이터 유효성 검사(validation)와 설정 관리(settings management)를 위한 라이브러리로 데이터를 깔끔하고 정확하게 처리하는 데 도움을 줍니다. 예를 들어, 어떤 프로그램이나 애플리케이션에서 정보를 입력받을 때, Pydantic은 그 정보가 올바른 형식인지 확인해줍니다.
- Swagger UI와 ReDoc을 사용하여 자동으로 API 문서를 생성
- 비교적 새로운 프레임워크이므로, Django나 Flask와 같은 오래된 프레임워크에 비해 커뮤니티가 작고, 사용자 기반과 자원이 상대적으로 적다.

## 서버 시작, 로깅, 디버깅에 대한 화면 캡처와 설명

## HTTP 메서드를 통해 서버에 요청을 보내고 응답을 받았을 때의 화면, 헤더, 바디 캡처 및 설명

## API 서버의 구현 방법과 주요 기능에 대한 설명

# Assignment2

## Table Specifications
```python3
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
```

# Assignment3

## 1) Pre-trained Model
- 모델과 가중치는 [DeepLabv3](https://github.com/KimRass/DeepLabv3)에서 가지고 왔습니다.
- 'deeplabv3-voc2012.pth'를 'resources' directory에 위치시킵니다.

## 2) How to run
