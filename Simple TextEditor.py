
class CustomStack:
    
    def __init__(self):
        self.texts=[]
        self.undoop=0
        self.undotext=[]

    def insert(self, text):
        # print(text)
        for c in text:
            self.texts.append(c)
        self.undotext=text
        self.undoop=1

    def delete(self, index):
        delete = min(index, len(self.texts))
        print("delete:",delete)
        self.undotext=""
        undotext=""
        for _ in range(delete):
            undotext += self.texts.pop()
        self.undotext = undotext[::-1]
        self.undoop=2
  
    def get(self, index):
        # print(index)
        print(self.texts)
        return self.texts[index-1]
    
    def undo(self):
        print(self.undotext)
        if (self.undoop==2):
            for c in self.undotext:
                self.texts.append(c) 
        if(self.undoop==1):
            for c in self.undotext:
                self.texts.pop()
        return

    # def get(string,index):
    #     for i in range(len(string)):
    #         if(index==string[i]):
    #             print(string)

editor = CustomStack()
val = input()
val_split = val.split(",")
print(val_split)
textEditor=[]
for i in range(len(val_split)):
    textEditor=val_split[i].split(' ')
    if(textEditor[0]=='1'):
        editor.insert(textEditor[1])
    elif(textEditor[0]=='2'):
        editor.delete(int(textEditor[1]))
    elif(textEditor[0]=='3'):
        print(editor.get(int(textEditor[1])))
    elif(textEditor[0]=='4'):
        print(editor.undo())
# 1 abc,3 3,2 2,3 1



# while True:
#     print("1:insert 2:delete 3:get 4:display")
#     choice=int(input("enter the choice:"))
#     if(choice==1):
#         text=input("enter the")
#         customStack.insert(text)
#     elif(choice==2):
#         delete = customStack.delete()
#         print("deletion:",delete)
#     elif(choice==3):
#         customStack.display()