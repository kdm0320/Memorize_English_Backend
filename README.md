# 영어단어 암기 API Project - Backend

## Description

영어단어 암기 API의 Backend Repo입니다  
Python의 웹프레임워크인 Django로 구성했으며  
Django-RestFramework를 사용했습니다.

---

## Backend URL

## https://voca-back.herokuapp.com

## Used Language & Libraries

- ### Python

- ### Django
- ### Django-RestFramework

---

## Content - API별 기능 상세설명

- ### api/v1/words/
  - 저장된 단어 세트 리스트를 보여줌
  - Read는 누구나 가능하나 그 밖의 Method는 admin 유저만 가능
- ### api/v1/users/
  - Create - 누구나 가능
  - Read - admin 유저만 가능
  - Update, Delete 인증된 유저만 가능
- ### api/v1/qnaboards/

  - Create,Read - 누구나 가능
  - Update, Delete 작성한 유저만 가능

---

## 관련 URL

- ### 프로젝트 URL : https://memovoca.shop

- ### Frontend: https://github.com/kdm0320/Memorize_English_Frontend.git

## Reference

- ### 토익 빈출영어단어 327
  https://bonlivre.tistory.com/75
- ### 기본 영어단어 1000개
  https://m.blog.naver.com/cu1023/221296679654
