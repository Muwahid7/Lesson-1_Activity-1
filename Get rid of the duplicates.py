student_data = {'id_1':{'name':['Sarah'],'class':['V'],'subject_integration':['english,math,science']},
'id_2':{'name':['Harry'],'class':['VI'],'subject_integration':['social,math,science']},
'id_3':{'name':['Sarah'],'class':['V'],'subject_integration':['english,math,science']},
'id_4':{'name':['Larry'],'class':['VII'],'subject_integration':['english,social,science']},}
result = {}
for  key,value in student_data.items():
    if value not in result.values():
        result[key]=value
print(result)
