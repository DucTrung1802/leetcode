class MyHashMap:

    def __init__(self):
        self.hash = 1000
        self.buckets = [[] for _ in range(self.hash)]

    def put(self, key: int, value: int) -> None:
        bucketIdx = key % self.hash
        for i in range(len(self.buckets[bucketIdx])):
            if self.buckets[bucketIdx][i][0] == key:
                self.buckets[bucketIdx][i][1] = value
                return
        self.buckets[bucketIdx].append([key, value])

    def get(self, key: int) -> int:
        bucketIdx = key % self.hash
        for k, v in self.buckets[bucketIdx]:
            if k == key:
                return v
        return -1
        
    def remove(self, key: int) -> None:
        bucketIdx = key % self.hash
        for i in range(len(self.buckets[bucketIdx])):
            if self.buckets[bucketIdx][i][0] == key:
                self.buckets[bucketIdx].pop(i)
                return


# Your MyHashMap object will be instantiated and called as such:
myHashMap = MyHashMap()
myHashMap.put(1, 1)
myHashMap.put(2, 2)
myHashMap.get(1)
myHashMap.get(3)
myHashMap.put(2, 1)
myHashMap.get(2)
myHashMap.remove(2)
myHashMap.get(2)
