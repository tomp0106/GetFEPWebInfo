from WebActions import SeleniumAction
import os

#取得已建立的文件並顯示
files = os.listdir('BOM')
if len(files)==1:
    MaterialSNFileName=files[0]
else:
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


ProductGroupName=MaterialSNFileName[0:MaterialSNFileName.find('.')]


#取得料件數量流程
MaterialSeacher=SeleniumAction()

print('進行登入作業....')

LoginStus=MaterialSeacher.LoginAction()

if LoginStus==1:
    SeachResultList=[]
    for MaterialSN in MaterialSNList:
        SeachResult=MaterialSeacher.SearchMaterialAction(MaterialSN.strip())
        if SeachResult!='':
            SeachResultList.append(SeachResult)

    if len(SeachResultList)!=0:
        f = open('{}_SeachResult.csv'.format(ProductGroupName), 'w+')
        for SeachResultItem in SeachResultList:
            f.write(SeachResultItem + '\n')
        f.close()

MaterialSeacher.CloseBrower()