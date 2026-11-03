class MedianFinder:

    def __init__(self):
        self.median = None
        self.arr = []
        self.median_id = 0
        self.odd = False

    def addNum(self, num: int) -> None:
        print(self.arr)
        if 0<len(self.arr)<4:
            self.arr.append(num)
            self.arr.sort()
            if len(self.arr)==2:
                self.median_id=0
                self.median=sum(self.arr)/2
            elif len(self.arr)==3:
                self.median_id=1
                self.median=self.arr[1]
            elif len(self.arr)==4:
                self.median_id=1
                self.median=sum(self.arr[1:3])/2
                self.odd = True
            print("less than 3", self.arr, self.median, 'odd',self.odd)
        elif len(self.arr):
            if num>self.median:
                if num>self.arr[self.median_id+1]:
                    self.arr.append(num)
                    print("more median+1", self.arr)
                else:
                    self.arr = self.arr[:self.median_id+1]+[num]+self.arr[self.median_id+1:]
                    print("median+1", self.arr)
            elif num==self.median:
                self.arr = self.arr[:self.median_id+1]+[num]+self.arr[self.median_id+1:]
                print("median", self.arr)
            else:
                if num<self.arr[self.median_id-1]:
                    self.arr = [num]+self.arr
                    print("less median-1", self.arr)
                else:
                    self.arr = self.arr[:self.median_id]+[num]+self.arr[self.median_id:]
                    print("median-1", self.arr)
            if not self.odd:
                self.median_id = self.median_id
                self.median = (self.arr[self.median_id]+self.arr[self.median_id+1])/2
                print('became even', self.median)
            else:
                self.median_id += 1 
                self.median = self.arr[self.median_id]
                print('became odd', self.median)
            self.odd = not self.odd
        else:
            self.arr.append(num)
            self.median_id = 0
            self.median = self.arr[self.median_id]
            self.odd=True


    def findMedian(self) -> float:
        return self.median
        
        