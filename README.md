# Smeffi Message Server
스매피 통합 메시지 서버다.

## 개발 설정 (PyCharm 기준)
1. Python 3.9 설치 ([Python 3.9 다운로드](https://www.python.org/downloads/))
   1. Customize install location 설정 후 설치. `c:\Python\Pyhotn309` 추천
2. File -> Settings -> Project: honeyquikc2-was -> Python Interpreter 에서 우측 톱니바퀴 클릭 -> Add 클릭
3. Base Interpreter 에 `C:\Python\Python309` 폴더 선택.
4. Location 폴더 선택 (honeyquick2-was 하단에 venv 폴더 만든 후 선택)
5. requirements.txt 에 포함된 Python Package Install
6. main.py 실행.

---

## 배포 (AWS)
### AWS Elastic Beans Talk 구성 (1회) _*작성전_
1. 새 애플리케이션 생성
2. 환경생성
   1. 설정
   2. 환경변수 추가 (실서버: PROD, 테스트서버: DEV)


### 애플리케이션 배포
1. 아래 파일 및 폴더를 **.zip으로 압축** 후 파일명으로 버전 관리 (배포 환경에서 파일이름 중복 불가).
`app/`
`.dockerignore`
`Dockerfile`
`requirements.txt`

2. **AWS Elastic Beans Talk** 환경에 압축 파일 업로드.