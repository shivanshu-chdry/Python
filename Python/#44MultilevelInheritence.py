class Dad:
    basketball = 1

class Son(Dad):
    dance = 1
    def idance(self):
        return f'Yeah, I dance {self.dance} number of times'

class Grandson(Son):
    dance = 6
    def idance(self):
        return f'Yes, I dance {self.dance} number of times'

mike = Dad()
jack = Son()
josh = Grandson()

print(josh.idance())
print(josh.basketball)#This will also return 1