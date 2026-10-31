class Solution:
    def reverse(self, x: int) -> int:
        MASK = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF
        res = 0
        negative = False

        if x < 0:
            x = x * -1
            negative = True
        

        while x > 0:

            #1) Grab right most digit using modulo
            right_digit = x % 10
            
            #2) Stretch result tray by this amount
            res = res * 10
            #3) Add right most digit to tray
            res += right_digit
            #4) Shrink original number
            x = x // 10

        
        #if positive and in range return normal number
        if res <= MAX_INT:
            print(f"I am not out of bounds? {res}")
            if negative:
                return -res

            else:
                return res

        #out of range, return 0
        else:
            return 0


