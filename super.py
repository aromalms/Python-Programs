#program to implement super() function
class Family:
    def family_info(self):
        return 'Good'

class Father(Family):
    def father_info(self):
        status=super().family_info()
        print(status)
obj=Father()
obj.father_info()