class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars = sorted(zip(position, speed), reverse = True)
        
        for p, s in cars:
            arrival_time = (target - p) / s

            if not stack or arrival_time > stack[-1]:
                stack.append(arrival_time)
        return len(stack)
 

        