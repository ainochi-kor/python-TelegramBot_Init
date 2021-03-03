# telegrambot (클라우드를 이용한 텔레그램 챗봇 만들기)

<p align="center">
  <img src="https://systemscue.it/wp-content/uploads/2016/02/telegram_bot.jpg" width="600" height="450">
</p>
<br>

## 목차
- 목적설정
- 정보수집과 선택
- 현재의 상황 및 문제점
- 개선 및 제안(효과)
- 최종확인


### 1) 목적설정
① 무슨 이유로 만들게 되었는가? <br>
>  해외 또는 국내의 보안 메신저로 유명한 Telegram은 보안이 필요한 회사에서 특히 잘 쓰이고 있다. 회사에 입사하게 된다면 ‘카카오톡’뿐만 아니라 Telegram을 사용할 수 있다. Telegram에 대해서 알아보던 중 Bot API를 이용하여 여러가지 기능을 할 수 있는 것으로 알려졌다. 그리하여 작년부터 봇을 개발하던 중에 Web Crawling을 통해 날씨를 비롯하여 수 많고 다양한 기능을 추가하였다. 그러나 이전부터 가지고 있던 가장 큰 문제는 24시간동안 시스템을 가동시킬 수 있는 컴퓨터가 없다는 것이다. 이 클라우드 컴퓨팅 수업을 통하여 그 문제를 해결할 수 있었다. 
 그러나 시간이 지난 Telegram은 업데이트 하고 Telegram bot 또한 업데이트하여 인터넷에 올려져있는 간단한 Code들은 Bot의 시작 조차 불가능하다. 왜냐하면 함수식부터 다 바뀌었기 때문이다. 그리하여 사람에게 도움이 되고, 24시간동안 시스템을 가동시킬 수 있는 봇을 만들고 싶은 것은 내 오랜 소망이었기 때문에 만들게 되었다.

목표)
-	텔레그램 봇 API 주소를 얻기
-	텔레그램 봇 API를 서버에 가동시키기 전 코드 작성.
-	Pycharm을 이용하여 텔레그램 코드 테스트
-	테스트 완료 후, AWS와 Azure 클라우드에 넣고 실행하기
-	24시간 서버를 가동하는 봇 완성하기. 

### 2) 정보수집과 선택
- 기존에 가지고 있던 독자적으로 개발한 챗봇의 파이썬 코드를 가져와서 실행.
- 카카오톡 오픈 챗팅 및 커뮤니티를 이용하여 챗봇이 아닌 파이썬에 대한 지식을 보충.
- Telegram Bot API Help 사이트를 이용하여 영어를 해석하고 오류를 해결
- AWS의 ec2의 SageMaker 서비스를 이용함.
- Microsoft Azure Notebooks 서비스를 이용함.

### 3) 봇 API 얻기

![image](https://user-images.githubusercontent.com/48821257/109729039-aa0dbe80-7bfa-11eb-9981-73546173d4ca.png) <br>
1.	구글 주소 창에 텔레그램을 검색한다. <br>

![image](https://user-images.githubusercontent.com/48821257/109729118-beea5200-7bfa-11eb-8256-7230f74c2f02.png) <br>
2. 텔레그램 한글사이트를 클릭한다 (본 봇 API는 휴대폰에서도 얻을 수 있지만 PC화면 위주로 보여드리겠습니다.) <br>

![image](https://user-images.githubusercontent.com/48821257/109729324-0bce2880-7bfb-11eb-9d8d-e3452e2d7e57.png) <br>
3.윈도우 PC버전 다운로드 클릭 <br>

![image](https://user-images.githubusercontent.com/48821257/109729341-12f53680-7bfb-11eb-9a2b-36260e0e84ed.png) <br>
4. 텔레그램 다운로드 <br>

![image](https://user-images.githubusercontent.com/48821257/109729358-1983ae00-7bfb-11eb-9091-117b09838baf.png) <br>
5. English에서 Ok <br>
(로그인 화면에서는 한국어로 사용이 가능하기 때문에 English로 진행하도록 한다.) <br>
설치는 간단하기에 중략. <br>

![image](https://user-images.githubusercontent.com/48821257/109729391-23a5ac80-7bfb-11eb-9bd7-cbf636ceeec8.png) <br>
6. 한국어로 진행을 누른다. <br>

![image](https://user-images.githubusercontent.com/48821257/109729408-2accba80-7bfb-11eb-9355-6bab094df1e5.png) <br>
7.대화시작하기를 누른다. <br>

![image](https://user-images.githubusercontent.com/48821257/109729438-34562280-7bfb-11eb-9ec6-d9cfc12624ad.png) <br>
8.국가를 선택하고와 휴대폰 번호를 입력한다. <br>

![image](https://user-images.githubusercontent.com/48821257/109729469-3e782100-7bfb-11eb-83b0-2022e6518a3d.png) <br>
9.메인화면 <br>

![image](https://user-images.githubusercontent.com/48821257/109729490-48018900-7bfb-11eb-8a61-5e1d40096f59.png) <br>
10.검색 창에서 BotFather를 검색한다. <br>

![image](https://user-images.githubusercontent.com/48821257/109729513-4fc12d80-7bfb-11eb-8a6a-c529f1f8fa8f.png) <br>
11.봇에 대한 설명 읽기 <br>

![image](https://user-images.githubusercontent.com/48821257/109729533-58b1ff00-7bfb-11eb-892c-3aaa4804353f.png) <br>
12. 아무 말을 하면 명령어 양식을 줍니다. <br>

 ![image](https://user-images.githubusercontent.com/48821257/109729594-767f6400-7bfb-11eb-8856-21c0b67562a8.png) <br>
13. “/newbot”을 입력합니다. <br>
 
 ![image](https://user-images.githubusercontent.com/48821257/109729601-7aab8180-7bfb-11eb-85c2-385f0d9d07cc.png) <br>
14. 이름 하기 전 주의 사황 <br>
//bot은 이름 맨 마지막에 붙일 것 <br>
 
 ![image](https://user-images.githubusercontent.com/48821257/109729721-aa5a8980-7bfb-11eb-8b2b-2efbbf8fc377.png) <br>
15.제대로 된 이름 입력하기. <br>
//동그라미 친 곳을 누르면 봇에 입장합니다. <br>
//밑 줄 친 주소는 HTTP API입니다. <br>
 
 ![image](https://user-images.githubusercontent.com/48821257/109729737-afb7d400-7bfb-11eb-9c03-b9f97aea4181.png) <br>
16.봇에 입장하기. <br>

#### 이렇게 하면, 텔레그램 봇은 생성되었지만 기능이 없는 상태입니다.

<br>
<br>

 
### 4) 파이썬 개발환경 설치하기(테스트용)  <br>
![image](https://user-images.githubusercontent.com/48821257/109729840-da099180-7bfb-11eb-8bb6-636b66fbb2f0.png)  <br>
1.구글 검색 엔진에 아나콘다를 검색한다.  <br>

![image](https://user-images.githubusercontent.com/48821257/109729882-e988da80-7bfb-11eb-9ecb-d15564369bda.png)  <br>
2. 아나콘다 홈페이지로 들어간다.  <br>

![image](https://user-images.githubusercontent.com/48821257/109729959-10dfa780-7bfc-11eb-925c-86e1295c8bba.png)  <br>
3.다운로드를 누른다.  <br>
 
![image](https://user-images.githubusercontent.com/48821257/109729972-15a45b80-7bfc-11eb-8ab0-5399d8939457.png)  <br>
4. Windows를 클릭하고 Python3.7 version 다운로드를 누른다.  <br>
 
![image](https://user-images.githubusercontent.com/48821257/109729989-1937e280-7bfc-11eb-9b96-5b7b723d08a0.png)  <br>
5.구글에 파이참을 검색한다  <br>

![image](https://user-images.githubusercontent.com/48821257/109730001-1ccb6980-7bfc-11eb-941a-c8a97f9a682c.png)  <br>
6.다운로드를 누른다  <br>
 
![image](https://user-images.githubusercontent.com/48821257/109730015-21901d80-7bfc-11eb-953e-edd33a3179a6.png)  <br>
7. 글로벌 학생증을 소유하고 있으면 구매하지 않고도 프로페셔널을 다운 받을 수 있다.  <br>
 
![image](https://user-images.githubusercontent.com/48821257/109730045-2fde3980-7bfc-11eb-8a4d-97a511520190.png)  <br>
8.하단에 노란 형광펜으로 칠한 터미널을 클릭하고 터미널에  <br>
```
Pip install telegram
Pip install python-telegram-bot
Pip install requests
Pip install request
Pip install beautifulsoup4
```
를 입력해준다.  <br>

 ![image](https://user-images.githubusercontent.com/48821257/109730067-3a003800-7bfc-11eb-8ef1-5d9b543206e4.png)  <br>
9.파이썬 스크립트에 복사해서 붙여넣도록 하여 테스트 하도록 한다.  <br>
 
 ![image](https://user-images.githubusercontent.com/48821257/109730083-41274600-7bfc-11eb-801b-22c0dfbd9669.png)  <br>
10.테스트.  <br>
‘모해’를 입력하면 ‘얍’을 출력하는 것을 알 수 있음.  <br>
[텔레그램 테스트 완료]  <br>


[azure 주피터 노트북 실행] <br>
 ![image](https://user-images.githubusercontent.com/48821257/109730113-50a68f00-7bfc-11eb-8f54-9286591493d9.png) <br>
1.	구글에 azure jupyter notebook <br>

 ![image](https://user-images.githubusercontent.com/48821257/109730130-556b4300-7bfc-11eb-9653-2f55d9abacf5.png) <br>
2.Try It Now 클릭 <br>
 
![image](https://user-images.githubusercontent.com/48821257/109730609-17baea00-7bfd-11eb-996a-1085fb8c6e73.png) <br>
3.	파이썬 클릭하고 Run을 클릭 <br>
 
![image](https://user-images.githubusercontent.com/48821257/109730178-6b790380-7bfc-11eb-8d80-72c856a9c532.png)  <br>
4.	개설하였으면 파이썬을 누르고 다시 런을 누른다. <br>
 
![image](https://user-images.githubusercontent.com/48821257/109730183-6f0c8a80-7bfc-11eb-8ac8-acaa6aed1c76.png) <br>
5.	주피터에 들어온 것을 알 수 있다.  <br>

![image](https://user-images.githubusercontent.com/48821257/109730188-72a01180-7bfc-11eb-80e1-2124dc460d9a.png) <br>
6.	new에서 Terminal로 들어간다.   <br>

![image](https://user-images.githubusercontent.com/48821257/109730201-7895f280-7bfc-11eb-8d59-d95965584cba.png) <br>
7.	터미널로 들어온 화면. <br>

![image](https://user-images.githubusercontent.com/48821257/109730449-d4607b80-7bfc-11eb-9a5a-c95d1675a2d9.png) <br>
8.이 코드를 주피터 노트북에 입력한다.  <br>

![image](https://user-images.githubusercontent.com/48821257/109730454-d88c9900-7bfc-11eb-8b35-910a95f3ece0.png) <br>
9.마지막 까지 입력 시 뜨는 터미널 화면. <br>

![image](https://user-images.githubusercontent.com/48821257/109730469-dde9e380-7bfc-11eb-9c9c-e278635eb1a1.png)  <br>
10.new에 새로운 환경이 생긴 것을 볼 수 있다. <br>
 
![image](https://user-images.githubusercontent.com/48821257/109730473-dfb3a700-7bfc-11eb-92a2-816d006eacbf.png) <br>
11.venv_test0_python36을 클릭하면 이 화면을 볼 수 있다. <br>
 
![image](https://user-images.githubusercontent.com/48821257/109730481-e2160100-7bfc-11eb-9ca8-60f4c0e31445.png) <br>
12.파이참에서 사용했던 코드를 가져온다. <br>

![image](https://user-images.githubusercontent.com/48821257/109730829-7a13ea80-7bfd-11eb-846e-aeb054c91404.png) <br>
13. 텔레그램 챗봇이 정상적으로 돌아가는 것을 알 수 있다. <br>

### 4) 개선 및 제안(효과)  <br>
![image](https://user-images.githubusercontent.com/48821257/109730841-7f713500-7bfd-11eb-8030-b8c3e38ac232.png) <br>
업데이트 이전 여러가지 기능을 가능하게 했던 봇으로 되살리기.  <br>
함수에 대한 이해를 더 하면 가능할 것으로 보임.  <br>



### 5) 소감  <br>
 제가 쓴 코드를 그대로 복사 붙여넣기 하는 것보다 파이썬의 대한 이해를 바탕으로 직접 쓸 수 있게 만드는 것이 좋겠다고 생각하여 제가 쓴 코드를 모두 레포트에 적지 않고, 정말 초급자 분들이 텔레그램 봇을 이용할 때 기초환경을 만들도록 작성하였습니다. 이것을 보고도 짜기 힘들 수도 있지만 https://core.telegram.org/bots/api 를 통하여 해석이 가능하다면 참고하셔도 좋을 것 같다고 생각합니다. 공식 텔레그램 api 사이트입니다.  <br>
 
