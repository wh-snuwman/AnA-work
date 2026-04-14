import datetime
from  random import randint


class Student():
    def __init__(self,name,age=18,number=10000,birth=''):
        if type(age) != int:
            print("나이가 숫자가 아닙니다! 기본값으로 초기화 됩니다.")
            
        if type(number) != int:
            print("나이가 숫자가 아닙니다! 기본값으로 초기화 됩니다.")

        self.name = name
        self.age = age
        self.number = number
        self.birth = birth


    def sayhello(self):
        print(f"안녕하세요. 저는{self.name} 입니다.") 
        print(f"나이는 {self.age} 이고 학번은 {self.number}입니다.") 
        print(f"생일은 {self.birth}입니다.") 

    def isSchool(self):
        if (datetime.date.isoweekday(datetime.date.today())) > 5:
            print("오늘은 학교에 가는날이 아닙니다.")

        else:
            print("학생은 학교에 가는날 입니다.")


class Han(Student):
    def __init__(self,name,age,number,birth):
        super().__init__(name,age,number,birth)
        self.gender = 'man'
        self.club = 'AnA' # Attack n Attack
        self.isHansome = True

    def R_u_going_to_buy_us_a_snack_bar(self):
        yes = 0 < randint(0,100)
        if yes:
            print(f"{self.name}님이 {self.club}모두에세 간식을 사주신다고 하십니다.")
        else:
            print(f"간식대신에 {self.name}님이 {self.club}모두에세 아웃백을 쏜다고 하십니다.")



s = Han('장한울',18,12345,123456789)

s.sayhello()
s.isSchool()

s.R_u_going_to_buy_us_a_snack_bar()