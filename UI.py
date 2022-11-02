import tkinter as tk
from tkinter.scrolledtext import ScrolledText


class SelectMenu():
    def __init__(self,ProductNameList):
        self.root = tk.Tk()
        self.root.geometry("250x200")
        self.root.title('物料獲取程式')
        self.text = ScrolledText(self.root, width=20, height=10)
        self.checkboxes = {}

        self.ProductNameList = ProductNameList
        self.SelectNameResult=[]



        #物件參數
        self.button = tk.Button(self.root,
                           text='Click',
                           command=self.RetrunProductNames)


        #版面配置
        for i in range(len(self.ProductNameList)):
            self.checkboxes[i] = tk.BooleanVar()  # 布林值變數
            self.checkboxes[i].set(1) #預設為選取

            cb = tk.Checkbutton(self.text, text=self.ProductNameList[i], variable=self.checkboxes[i], bg='white', anchor='w')

            self.text.window_create('end', window=cb)
            self.text.insert('end', '\n')

        self.text.pack()
        self.button.pack()
        self.root.mainloop()

    def RetrunProductNames(self):
        for i in self.checkboxes:
            if self.checkboxes[i].get() == True:
                self.SelectNameResult.append(self.ProductNameList[i])

        self.root.destroy()


if __name__ == '__main__':
    ProductNameList = ['ax', 'b', 'c']
    app = SelectMenu(ProductNameList)
    print(app.SelectNameResult)
