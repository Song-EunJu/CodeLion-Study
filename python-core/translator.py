from googletrans import Translator

# 1. 번역기 생성
translator = Translator() 

# 2. 언어 감지 원하는 문장 실행
sentence = input("번역할 문장을 입력해주세요 : ")
language = input("어떤 언어로 번역할까요? : ")

# 3. 언어 감지
detected = translator.detect(sentence) 

# 4. 번역 / translate(text,dest,src) : 번역할 문장, 어떤 언어로 번역할 것인지, 번역할 문장의 언어
result = translator.translate(sentence,language)

print("===========출 력 결 과===========")
print(detected.lang, ":", sentence)
print(result.dest, ":", result.text)
print("=================================")