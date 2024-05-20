import math

# 선분 object 생성 클래스
class Line:

    # 기본값 1 또는 전달받은 값으로 객체를 생성하는 생성자.
    # length 인수는 값을 전달 받으면 전달 받은 값을 __length 필드에 전달해주고
    # 값을 전달 받지 않으면 기본값인 1을 __length에 전달한다.
    def __init__(self, length = 1):
        self.__length = length
        # __length에서 __를 앞쪽에 지정하면 클래스 밖에서는 접근할 수 없다.

    # int, float로만 __length를 설정가능한 메소드
    def set_length(self,len):
        if isinstance(len, int) or isinstance(len, float):
        # len이 int or float 클래스의 객체일 때만 true를 반환
            if len>0:
            # 전달받은 len이 양수 일때만 __length에 len값 전달
                self.__length = len
            else:
            # 양수가 아니면 기본값인 1로 __length 설정
                if self.__length <=0:
                    self.length=1
        else:
        # len이 int, float값이 아니면 기본값인 1로 __length 설정
            self.__length=1

    # 외부에서 __length 값을 얻어오기 위해서는 같은 클래스의 함수 get_length를 이용해야만 가능하다.
    def get_length(self):
        return self.__length

# Line 객체를 전달받아 직사각형 넓이를 리턴하는 함수
def area_square(line):
    if isinstance(line, Line):
    # 전달받은 객체가 Line 클래스의 객체라면 
        return line.get_length()**2 
                # line 객체에서 __length값을 리턴받아 제곱해서 넓이를 리턴하고
    else:
    # Line 클래스의 객체가 아니라면
        return 0
                # 0을 리턴한다.
def area_circle(line):
    if isinstance(line, Line): 
        return line.get_length()**2*math.pi
    else:
        return 0
def area_regular_triangle(line):
    if isinstance(line, Line):
        return math.sqrt(3)/4*line.get_length()**2
    else:
        return 0
    
