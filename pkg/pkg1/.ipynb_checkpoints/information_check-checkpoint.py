class Info_Check():
    
    def __init__(self,name,iid):
        self.list = ["12345","54321"]
        self.name = name
        self.iid = iid
    
    def check_inlist(self):
        if self.iid.lower() in self.list:
            return True
        else:
            return False
        
    def check_IsNull(self):
        if self.name=="":
            return True
        else:
            return False
        

    