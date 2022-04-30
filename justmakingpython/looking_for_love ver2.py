total_list = []

while True :
    question = input("이상형 기준을 입력해주세요 : ")
    if question == 'q' or question == '그만' :
        break
    else :
        total_list.append({'질문' : question, '답변' : ""})
for i in total_list:
    print(i['질문'])
    answer = input('답변을 입력해주세요 : ')
    i['답변'] = answer
print(total_list)