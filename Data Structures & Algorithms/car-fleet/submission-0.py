class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # All position are unique => no more than one car starting at the same position
        # IDEA: if a car takes less time to reach the target than the car ahead, then it joins that car in a fleet
        # 1. Sort the cars based on their position in DESCENDING order. This way we are sure that the next car in the array (the very previous one in space) will join the fleet if and only if it takes less time to reach the target.
        # 2. Determine the time to target using the formula: speed = space / time =>
        #       time = space / speed where space = target - position =>
        #       time = (target - position) / speed
        # 3. Keep a stack for the identified fleet. If a car time is less than or equal
        #       to the head of stack than it joins the stack, otherwise it is appended

        fleets = [] # STACK for the fleets

        # 1. Array of tuples: for each car (pos, speed)
        cars = list(zip(position, speed))
        cars.sort(reverse=True) # Descending order with reverse=True

        # 2. Determine each car's time of travel
        for pos, spe in cars:
            time = (target - pos) / spe
            if fleets and fleets[-1] >= time:
                # joins the fleet, we do nothing
                continue
            else:
                # does not join the fleet, create a new fleet
                fleets.append(time)

        return len(fleets)
