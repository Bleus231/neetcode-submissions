from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        result = ""
        value_list = self.store.get(key, [])        
        left = 0
        right = len(value_list) - 1
        

        while left <= right:
            mid = (right + left) // 2

            #unpacking tuple values
            ts , value = value_list[mid]

            if ts <= timestamp:
                result = value
                left = mid + 1
            else:
                right = mid - 1

        return result