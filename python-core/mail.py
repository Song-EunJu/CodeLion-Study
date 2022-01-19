import smtplib # SMTP 메일 서버로 쉽게 메일을 보낼 수 있게 해주는 라이브러리
from email.message import EmailMessage # 이메일 내용을 MIME 타입으로 변환시켜주는 기능
import imghdr # 확장자 판단
import re # 정규표현식 사용

# 1. SMTP 메일 서버 연결
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465
smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)

def sendEmail(addr):
    reg = "^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$"
    if bool(re.match(reg, addr)):
        smtp.send_message(message)
        print("정상적으로 메일이 발송되었습니다.")
    else:
        print("유효한 이메일 주소가 아닙니다.")
    

# 이메일을 MIME 형태로 바꿔야 SMTP로 전송가능하므로 EmailMessage 라이브러리 사용
message = EmailMessage()
message.set_content("코드라이언 수업중입니다.")

message["Subject"] = "이것은 제목입니다."
message["From"] = "보내는 사람 이메일 주소"
message["To"] = "받는 사람 이메일 주소"

# file 을 open하고 자동으로 close까지 해줌
with open("./python-core/codelion.png","rb") as file:
    image_file = file.read()

# 동적으로 이미지 파일 확장자 가져오기
image_type = imghdr.what('codelion', image_file)
message.add_attachment(image_file, maintype="image", subtype=image_type)

# 2. SMTP 메일 서버에 로그인
smtp.login("구글 이메일 계정","구글 계정 비밀번호")
sendEmail(message["To"])
smtp.quit()

