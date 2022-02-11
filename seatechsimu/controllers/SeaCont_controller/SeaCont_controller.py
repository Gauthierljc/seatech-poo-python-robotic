
from controller import Robot, Motor,Camera,DistanceSensor,Keyboard

class RobotMotor(Motor):
    def __init__(self,name):
        super().__init__(name)
        self.setPosition(float('inf'))
        self.setVelocity(0)


class seatechrobot(Robot):
    def __init__(self):
        super().__init__()
        self.__leftMotor =RobotMotor('left wheel motor')
        self.__rightMotor =RobotMotor('right wheel motor')
        self.cam=Camera('camera')
        self.cam.enable(samplingPeriod=50)
        self.cam.recognitionEnable(samplingPeriod=50)
        self.ps7 = DistanceSensor('ps7')
        self.ps7.enable(samplingPeriod=50)
        self.ps0 = DistanceSensor('ps0')
        self.ps0.enable(samplingPeriod=50)

    def reconition(self):
            objs=self.cam.getRecognitionObjects()
            for obj in objs :
                inst=obj.get_colors()
                print(inst)
                size=obj.get_size_on_image()
                print(size)
                if inst == [1,0,0] and size[0]*size[1]>40:
                    self.runback()
                    #inst=0
                    print(inst)
                    
                else:
                    self.search()

    def run(self):
        self.__leftMotor.setVelocity(MAX_SPEED)
        self.__rightMotor.setVelocity(MAX_SPEED)

    def runback(self):
        self.__leftMotor.setVelocity(-MAX_SPEED)
        self.__rightMotor.setVelocity(-MAX_SPEED)
    
    def search(self):
        self.__leftMotor.setVelocity(MAX_SPEED)
        self.__rightMotor.setVelocity(-MAX_SPEED)


if __name__ =='__main__':

    
    TIME_STEP = 64
    MAX_SPEED = 6.28
    robot = seatechrobot()
    print("Hi")
    robot.run()
    
    print(" Hit")

    while robot.step(TIME_STEP) != -1:
        robot.reconition()
        pass