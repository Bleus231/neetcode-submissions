class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
       

        sorted_cars = list(zip(position,speed))
        sorted_cars.sort()
        reversed_cars = sorted_cars[::-1]
        stack = []

        for p,s in reversed_cars:
            time_to_target = (target - p) / s
            if stack and time_to_target <= stack[-1]:
                continue
            
            # Otherwise, it forms a new fleet
            stack.append(time_to_target)


        return len(stack)
        