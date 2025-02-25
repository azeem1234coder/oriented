class pair_elements:
    def twosums(self, nums, target):
        Lookup = {}
        for i, num in enumerate(nums):
            if target - num in Lookup:
               return (Lookup[target - num], i )
            Lookup[num] = i
value = int(input("Enter sum for which you want to make this search :"))
print("index1=%d, index2=%d" % pair_elements().twosums((10,20,30,40,50,60,70),value))
