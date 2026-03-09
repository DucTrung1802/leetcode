class MyHashSet:

    def __init__(self):
        self.bucket_size = 1000
        self.buckets = [[] for _ in range(self.bucket_size)]

    def add(self, key: int) -> None:
        index = key % self.bucket_size
        if key not in self.buckets[index]:
            self.buckets[index].append(key)

    def remove(self, key: int) -> None:
        index = key % self.bucket_size
        if key in self.buckets[index]:
            self.buckets[index].remove(key)

    def contains(self, key: int) -> bool:
        index = key % self.bucket_size
        return key in self.buckets[index]


# Your MyHashSet object will be instantiated and called as such:
my_hash_set = MyHashSet()
my_hash_set.add(1)
my_hash_set.add(2)
my_hash_set.contains(1)
my_hash_set.contains(3)
my_hash_set.add(2)
my_hash_set.contains(2)
my_hash_set.remove(2)
my_hash_set.contains(2)
print(my_hash_set.buckets)
