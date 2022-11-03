from math import sin,cos, pi


class SVGDraw:
    height = 500
    width = 500

    def __init__(self):
        pass
    

    def size(self,h,w):
        
        self.height = h
        self.width = w

    def drawCircle(self,x,y,radius):
        r2 = radius ** 2
        
        r = abs(x**2 + y**2)**(0.5)
        
        # negative bound
        if x < 0: raise Exception("x-cordinate is can not be negative")
        if y < 0: raise Exception("x-cordinate is can not be negative")

        # positive bound
        if x > self.width: raise Exception("x-cordinate is exceeding width")
        if y > self.height: raise Exception("x-cordinate is exceeding width")

        points = []

        # collecting all the points on the circumference
        theta = 0
        while theta<360: 
        
            angle = theta*pi/180        # angle in radian
            
            a,b = x,y
            
            
            #(x−xC)2+(y−yC)2=R2⟺(x,y)=(xC+Rsinθ0,yC+Rcosθ0)


            _x = x + radius*sin(theta)
            _y = y + radius*cos(theta)
            
            
            

            points.append((_x,_y))

            theta += 0.1

        #draw points
        self.draw(points)

        
    def draw(self, points):
        points_str = " ".join([ "%s,%s"%(p[0],p[1]) for p in points])

        polygon = "<polygon points='%s'  style='fill:lime;stroke:purple;stroke-width:1'/>"%(points_str)

        svg = "<svg height='%s' width='%s'> %s </svg>"%(self.height,self.width,polygon)

        html = "<html><body>%s </body </html>"%(svg)

        with open("render.html","w+") as f:
            f.write(html)
            f.close()



        
