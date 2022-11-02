from WebActions import SeleniumAction
from UI import SelectMenu
import os

#取得已建立的文件並顯示
FileNames = os.listdir('BOM')
if len(FileNames)==1:
    MaterialSNFileNameList=FileNames
else:
    app = SelectMenu(FileNames)

    #取得要獲取的料號資訊
    MaterialSNFileNameList=app.SelectNameResult

    if len(MaterialSNFileNameList)>0:
        print('已選擇項目:')
        for SelectItem in MaterialSNFileNameList:
            print(SelectItem)
    else:
        input('我都預設好給你了不要亂啦~~~~')
        os._exit()


#取得料件數量流程
MaterialSeacher=SeleniumAction()
print('進行登入作業....')
LoginStus=MaterialSeacher.LoginAction()

for MaterialSNFileName in MaterialSNFileNameList:

    f=open('./BOM/'+MaterialSNFileName,'r')
    MaterialSNList=f.readlines()
    f.close()

    ProductGroupName=MaterialSNFileName[0:MaterialSNFileName.find('.')]
    print('執行{}料件搜尋...\n'.format(MaterialSNFileName))
    if LoginStus==1:
        SeachResultList=[]
        for MaterialSN in MaterialSNList:
            SeachResult=MaterialSeacher.SearchMaterialAction(MaterialSN.strip())
            if SeachResult!='':
                SeachResultList.append(SeachResult)
            else:
                ErrRetryTimes=2
                for x in range(ErrRetryTimes):
                    SeachResult = MaterialSeacher.SearchMaterialAction(MaterialSN.strip())
                    if SeachResult!='':
                        SeachResultList.append(SeachResult)
                        break
                    if x ==ErrRetryTimes+1:
                        print('')


        if len(SeachResultList)!=0:
            f = open('{}_SeachResult.csv'.format(ProductGroupName), 'w+')
            for SeachResultItem in SeachResultList:
                f.write(SeachResultItem + '\n')
            f.close()

MaterialSeacher.CloseBrower()