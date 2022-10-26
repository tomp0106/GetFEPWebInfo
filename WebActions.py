from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs
import time

class SeleniumAction:
    def __init__(self):
        # 不讓瀏覽器執行在前景，而是在背景執行
        self.options  = webdriver.ChromeOptions()
        self.options.add_argument('--headless')
        self.driver = webdriver.Chrome(chrome_options=self.options, executable_path='./chromedriver')
        self.RetryNum=0



    def LoginAction(self):
        try:
            # 進行登錄作業
            self.driver.get("http://118.163.153.124:8083/login.aspx")
            FEPAccount = self.driver.find_element_by_id('TextBox1')
            FEPAccountPSW = self.driver.find_element_by_id('TextBox2')
            FEPAccountLoginBtn = self.driver.find_element_by_id('Button1')
            # 輸入資料與登入
            FEPAccount.send_keys('tomtsai')
            FEPAccountPSW.send_keys('0106')
            FEPAccountLoginBtn.click()
            return 1
        except :
            print('登入失敗!!!!')
            return 0

    def SearchMaterialAction(self,ProductGroupName,MaterialSN):
        #轉移至料件頁面
        self.driver.get("http://118.163.153.124:8083/materials/materials.aspx")
        # 進行搜尋動作
        MaterialSeach = self.driver.find_element_by_id('ContentPlaceHolder1_mam1_part_no')
        MaterialSeach.send_keys(MaterialSN + Keys.ENTER)
        # 搜尋緩衝
        time.sleep(0.1)

        soup = bs(self.driver.page_source, 'lxml')

        try:
            MaterialTable = soup.find(id='ContentPlaceHolder1_GridView1')
            MaterialTableTd = MaterialTable.find_all('td')

            if MaterialTableTd[2].get_text()==MaterialSN:
                MS=self.driver.find_element_by_id('ContentPlaceHolder1_GridView1_safety_stock_S_0').text

                SeachResult='{},{},{}'.format(MaterialSN,MaterialTableTd[3].get_text(),MS)
                print(SeachResult)
                f=open('{}_SeachResult.csv'.format(ProductGroupName),'a+')
                f.write(SeachResult+'\n')
                f.close()

            else:
                print('資料錯誤,重新搜尋!')
                self.SearchMaterialAction(ProductGroupName,MaterialSN)

        except :
            print('無此料號!!!')


    def CloseBrower(self):
        self.driver.quit()

if __name__ == '__main__':

    se = SeleniumAction()
    se.LoginAction()
    se.SearchMaterialAction('Test','A0003-000003')
    se.SearchMaterialAction('Test', 'F0002-000001')
    se.SearchMaterialAction('Test', 'E0017-000001')
    se.CloseBrower()

