class Solution:
    def internalAngles(self, sides: list[int]) -> list[float]:
        a,b,c=sorted(sides)
        if a+b<=c:
            return []
        A=math.degrees(math.acos((b*b+c*c-a*a)/(2*b*c)))
        B=math.degrees(math.acos((a*a+c*c-b*b)/(2*a*c)))
        C=180-A-B
        return sorted([A, B, C])