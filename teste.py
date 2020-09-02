class Car:
    def __init__(self, max_speed):
        self.max_speed = max_speed
        self.current_speed = 0

    def throtle(self, delta):
        self.current_speed += delta
        if self.current_speed > self.max_speed: self.current_speed = 180
        return self.current_speed
    
    def brake(self, delta):
        self.current_speed -= delta
        if self.current_speed < 0: self.current_speed = 0
        return self.current_speed

if __name__ == '__main__':
    c1 = Car(180)

    for _ in range(25):
        print(c1.throtle(8))

    for _ in range(10):
        print(c1.brake(20))
