import employee as E

class times:
    def __init__(self):
        self.max = 0
        self.current = 0
        self.name = []
    
    def time0(self):
        self.max = 2
    
    def time1678(self):
        self.max = 3
    
    def time2345(self):
        self.max = 4

class timetable:
    def __init__(self):
        self.cell = []

    def set_cell(self):
        for i in range(9):
            self.cell.append(list())
            for j in range(5):
                self.cell[i].append(times())


    def set_max(self):
        for i in range(9):
            for j in range(5):
                if i == 0:
                    self.cell[i][j].time0()
                elif 1 < i < 6:
                    self.cell[i][j].time2345()
                else:
                    self.cell[i][j].time1678()

def day_of_week(num):
    print({0:"MON", 1:"TUE", 2:"WEN", 3:"THU", 4:"FRI"}.get(num, "default"))

def time_of_day(num):
    print({0:"0교시", 1:"1교시", 2:"2교시", 3:"3교시", 4:"4교시", 5:"5교시", 6:"6교시", 7:"앞야", 8:"뒷야"}.get(num, "default"))