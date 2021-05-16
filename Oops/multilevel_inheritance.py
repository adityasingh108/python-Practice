class Electronic_Gadget:
    Electrictic = True
    Hardware= True

class pocket_Gadget(Electronic_Gadget):
    portable = True
    Chargebale = True


class mobile(pocket_Gadget):
    no_of_chrging = 4

    def no_of_chrged(self):
        return f"the chargebale time oof the mobile is {self.no_of_chrging}"

charger =Electronic_Gadget()
all_out = pocket_Gadget()
realme= mobile()



print(realme.no_of_chrged())
print(all_out.Electrictic)
print(realme.portable)
#print(all_out.no_of_charged())    this does't work this the function because it has no attributes 
 