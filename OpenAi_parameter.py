import xlsxwriter
import openai

workbook = xlsxwriter.Workbook('OpenAiParameters.xlsx')
worksheet = workbook.add_worksheet('firstsheet')

worksheet.write(0,0,'#')
worksheet.write(0,1,'temperature')
worksheet.write(0,2,'max_toke')
worksheet.write(0,3,'frequency_penalty')
worksheet.write(0,4,'presence_penalty')
worksheet.write(0,5,'top_p')
worksheet.write(0,6,'best_of')
worksheet.write(0,7,'token usage')
worksheet.write(0,8,'input')
worksheet.write(0,9,'output')


temperature = [0.01,0.25,0.5,0.75,1]
max_token=[100,500,25]
f_penelty=[0.01,0.5,1,1.5,2]
p_penelty=[0.01,0.5,1,1.5,2]
top_p=[0.01,0.25,0.5,0.75,1]
best_of=[2,10,20]
data1=[]
count=0
for a in temperature:
    for b in max_token:
        for c in f_penelty:
            for d in p_penelty:
                for e in top_p:
                    for f in best_of:
                         openai.api_key = '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'
                         count = count + 1
                         response = openai.Completion.create(
                                 model="text-davinci-002",
                                 prompt="can you help me decide my career?",
                                 temperature=a,
                                 max_tokens=b,
                                 top_p=e,
                                 frequency_penalty=c,
                                 presence_penalty=d,
                                 best_of=f
                                 )
                         text = response['choices'][0]['text']  
                         usage= response['usage']['total_tokens']
                         data = {'temperature':str(a) ,'max_tokens': str(b) ,'frequency_penalty': str(c), 'presence_penalty': str(d) ,'top_p': str(e), 'best_of': str(f),'usage':usage, 'input':"can you help me decide my career?",'output':text}
                         data.append(data)
print(count)  
daata2 = data1
for index,entry in enumerate(daata2) :
         worksheet.write(index+1,0,str(index))
         worksheet.write(index+1,1,entry['temperature'])
         worksheet.write(index+1,2,entry['max_tokens'])
         worksheet.write(index+1,3,entry['frequency_penalty'])
         worksheet.write(index+1,4,entry['presence_penalty'])
         worksheet.write(index+1,5,entry['top_p'])
         worksheet.write(index+1,6,entry['best_of'])
         worksheet.write(index+1,7,entry['usage'])
         worksheet.write(index+1,8,entry['input'])
         worksheet.write(index+1,9,entry['output'])

workbook.close()








                        
     
