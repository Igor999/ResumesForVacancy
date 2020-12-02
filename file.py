import pandas as pd
from datetime import timedelta, datetime
import smtplib

smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.starttls()
smtpObj.login('your google mail', 'your password')


try:
    self.smtp.ehlo()
    self.smtp.starttls()
    self.smtp.ehlo
except:
    print("No TLS :(")

jobs = pd.read_excel("lists.xlsx", sheet_name='A')
resume = pd.read_excel("lists.xlsx", sheet_name='B')

with open('time.txt', 'w') as op:
    if op.read() == (str(datetime.now().strftime("%Y-%m-%d"))):
        op.write(str(datetime.now().strftime("%Y-%m-%d") + timedelta(7).strftime("%Y-%m-%d")))

        resume = resume[resume['Дата'] > datetime.now() - timedelta(7)]
        resume = resume[resume['Правка резюме пройдена'] == True]

        list = set(map(int, resume["ID вакансии"].values))

        for number in list:
            jobs1 = jobs[jobs["requestid"] == number]
            lsts = resume[resume["ID вакансии"] == number]
            strings_for_mail = ""
            mail = jobs1["Контактный email"][0]
            for i in lsts:
                strings_for_mail += str(lsts[i])
            strings_for_mail = strings_for_mail.encode('utf8')
            smtpObj.sendmail("semenow.igorek@gmail.com", mail, strings_for_mail)
        smtpObj.quit()
        # print(str(lsts[i]))
        # strings += str(lsts[i])
    # print(lsts)
# print(strings)
    #
# print(list)



# print(resume)

# filter1 = resume['Название вакансии'] == 'Прогер'
# resume.where(filter1, inplace = True)
# print(resume)