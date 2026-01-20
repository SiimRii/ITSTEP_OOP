

class Time:
    """
    is representing time in hours and minutes
    """

    def __init__(self, hs, mins):
        if mins < 0:
            raise ValueError("Minutes cannot be negative.")
        elif mins >= 60:
            extra_hours = int(mins // 60)
            mins = mins % 60
            hs += extra_hours

        self.hours = hs
        self.minutes = mins


    def __str__(self):
        return f"{self.hours:02d}:{self.minutes:02d}"


    def __add__(self, other):
        total_mins = self.minutes + other. minutes
        total_hours = self.hours + other.hours
        if total_mins >= 60:
            extra_hours = int(total_mins // 60)
            total_mins = total_mins % 60
            total_hours += extra_hours
        return Time(total_hours, total_mins)


    def __eq__(self, other):
        return self.hours == other.hours and self.minutes == other.minutes


#########################################################################################


time1 = Time(2, 15)
time2 = Time(1, 75)


print("Time 1:", time1)
print("Time 2:", time2)
print()

final_time = time1 + time2
print("Final added time is:", final_time)

print("Are the two times equal?:", time1 == time2)