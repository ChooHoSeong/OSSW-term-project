# 모션인식 마우스

__개발 기획__

### 요약

OpenCV를 활용해 실시간으로 손 모양을 인식하고, 그에 따른 마우스 기능을 활성화하는 것

## 기능 명세서

__여기에 적힌 목록대로 모듈을 개발하면 될 듯__

1. OpenCV를 활용한 실시간 손 모양 인식  
기존에 구현된 걸 활용 -> 참조했다는 사실을 꼭 명시해야 함  
웹캠으로 손의 위치와 손가락 관절을 인식함

2. 손 모양 정의
손의 모양이나 움직임에 따라서 컴퓨터가 마우스 기능과 관련된 모양이라고 판단할 수 있어야 함

3. 손 모양에 따른 마우스 기능 구현
소프트웨어로 하드웨어의 기능을 쓸 수 있는지 확인할 것  
\* 구현해야하는 마우스 기능
	- 커서 위치 이동
    - 좌클릭 1번
    - 좌클릭 2번 (더블클릭)
    - 좌클릭 꾹
    - 우클릭
    - 휠 스크롤
    - 휠 클릭
    
## 해야할 일

1. 개발: 위의 기능 명세서에 맞춰 실제로 개발하기
2. 문서화: 프로젝트와 관련된 모든 걸 문서로 정리
3. 버전 관리: 깃허브를 활용해 깔끔하게 하는 것이 중요

## 프로젝트를 진행하며 지킬 것

### 1. 깃 & 깃허브

1. 모든 기능을 구현하고 깃에 올리지 말고, 세부적으로 그날 개발한 내용을 커밋한다.
2. commit, fetch, reset 등, 깃허브 쓸 줄 모르면, 공부해오자 (중요)  
~~\* 커밋이 겹쳐서 파일 꼬이게 만들면.... (검열)해버린다?~~
3. 커밋할 때, 이름이나 설명은 영어로 적고 자신이 건든 파일이 무엇인지, 어떤 부분을 수정했는지 핵심만 정리해서 올리자.
4. 모든 개발은 master(or main) 브랜치에서 진행하고, 오류, 테스트, 메인이 아닌 기능을 구현할 때는 새로 브랜치를 만들자.  
이때 기존의 브랜치를 이용하는 것이 아닌, 새로운 브랜치를 만들 것!

### 2. 개발

1. 파일은 소문자와 언더바(\_)만 (ex. main_file.py)  
   함수와 변수는 다음처럼 영어 대소문자만 (ex. def sumTable(), detectedMotion = 0 )  
   클래스는 다음처럼 영어 대소문자만 (ex. class MotionMouse: )  
   써서 이름을 만들자
2. 주석을 깔끔하게 달자. (복붙만 하지 말고, 주석을 수정한 다음 커밋하자)  
   그리고 주석은 변수, 함수, 클래스, 파일에 관한 내용을 적자.
3. 다른 곳에서 쓰일 것 같은 명칭은 팀원들에게 미리 얘기해서 두번 수정하지 않도록 하자.

### 3. 소통 (중요)

1. 커밋했으면, 했다고 말할 것
2. 톡방 확인은 신속하게