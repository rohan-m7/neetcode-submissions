class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}
        for i in s:
            hashmap[i] = hashmap.get(i, 0) + 1
        print(hashmap)
        for i in t:
            if i in hashmap:
                hashmap[i] -= 1
                if hashmap[i] == 0:
                    del hashmap[i]
            else:
                return False
        print(hashmap)
        return True if not hashmap else False
        