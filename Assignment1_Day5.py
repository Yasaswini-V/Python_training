


class Circle:
    def create(r):
        c=Circle()
        c.r=r
        return c

    def is_valid(c):
        return isinstance(c,Circle) and c.r>0 

    def perimeter(self,c):
        return 2*(22/7)*c.r if is_valid(c) else float('Nan')

    def area(self,c):
        return (22/7)*c.r*c.r if is_valid(c) else float('NaN')

    def info(self,c):
        return f'Circle <{c.r}>' if is_valid(c) else '<invalid triangle>'

    def draw(self,c,surface='Screen'):
        print(f'Drawing {self.radius} on {surface}')

def test_circle(r):
    c=create(r)
    c.draw(c)
    if is_valid(c):
        print(f"Area = {c.area(c)}")
        print(f"Perimeter = {c.perimeter(c)}")

test_circle(3)
