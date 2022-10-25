from WebActions import SeleniumAction
import os

#取得已建立的文件並顯示
files = os.listdir('BOM')
for x in range(len(files)):
    print(str(x)+'.'+files[x])

#取得要獲取的料號資訊
MaterialSNFileNameNumber=input('請輸入要搜尋的群組數字\n')

if MaterialSNFileNameNumber.isnumeric():
    MaterialSNFileName=files[eval(MaterialSNFileNameNumber)]
else:
    print('輸入"數字"!!看不懂中文喔!!!')

f=open('./BOM/'+MaterialSNFileName,'r')
MaterialSNList=f.readlines()
f.close()


ProductGroypName=MaterialSNFileName[0:MaterialSNFileName.find('.')]


#取得料件數量流程
MaterialSeacher=SeleniumAction()

print('進行登入作業....')

LoginStus=MaterialSeacher.LoginAction()

if LoginStus==1:
    for MaterialSN in MaterialSNList:
        MaterialSeacher.SearchMaterialAction(ProductGroypName,MaterialSN.strip())

MaterialSeacher.CloseBrower()