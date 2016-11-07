
class Time:

    def __init__(self, hour=0, min = 0 , sec = 0  ):
        self.hour = hour
        self.min = min
        self.sec = sec


    def __str__(self):
        return "{}:{:02d}:{:02d}".format(self.hour, self.min, self.sec)


    def __add__(self, other_time):
        new_time = Time()

        # Add the sec and correct if sum > 60
        if(self.sec + other_time.sec) >= 60:
            self.min += 1
            new_time.sec = (self.sec + other_time.sec) - 60
        else:
            new_time.sec = self.sec - other_time.sec

        # Add the min and correct if sum > 60
        if (self.min + other_time.min) >= 60:
            self.hour += 1
            new_time.min = (self.min + other_time.min) - 60
        else:
            new_time.min = self.min - other_time.min


        # Add the hour and correct if sum is > 24
        if(self.hour + other_time.hour) > 24:
            new_time.hour = (self.hour + other_time.hour) - 24
        else:
            new_time.hour = self.hour + other_time.hour

        return new_time


def main():
    time1 = Time(1, 20, 30)
    print time1

    time2 = Time(24, 41, 30)
    print time1+time2


main()
