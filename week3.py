class fal:
    def sel(self, first, second):
        self.first = first
        self.second = second

    def hap(self):
        result = self.first + self.second
        return result

a = fal()
a.sel(1, 2)

hap(a)
