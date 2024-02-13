class password:
    def __init__(self):
        self.s=0
        self.pass_dic={}
    def push(self,key,value):
        self.pass_dic[key]=value
        self.s+=1
        print(self.pass_dic)
    def find(self,key,value):
        if key in self.pass_dic:
            if self.pass_dic[key]==value:
                return True
            else:
                return "wrong password"
        else:
            return False
v=password()
v.push('kaviya','22hk')
print(v.find('kaviya','22hk'))
