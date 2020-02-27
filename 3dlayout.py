from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt 
import numpy as np
import cherrypy
# import request

class layout(object):
    
    # def __init__(self):
    #     global ax,plt
        
    @cherrypy.expose
    def update(self,p,q,r):
        global ax,plt
        fig= plt.figure()
        ax=plt.axes(projection="3d")
        # n=2
        m=4
        zline=np.linspace(0,m-1,10)
        for x in range(m):
            for y in range(m):
                xline = x+ np.zeros(len(zline))
                yline= y+ np.zeros(len(zline))
                ax.plot3D(xline,yline,zline,"gray")
        xline=np.linspace(0,m-1,10)
        for z in range(m):
            for y in range(m):
                zline=z+ np.zeros(len(xline))
                yline=y+np.zeros(len(xline))
                ax.plot3D(xline,yline,zline,"gray")
        yline=np.linspace(0,m-1,10)
        for x in range(m):
            for z in range(m):
                xline= x+np.zeros(len(yline))
                zline=z+np.zeros(len(yline))
                ax.plot3D(xline,yline,zline,"gray")
        if(p == '1' and q=='1' and r=='1'):
            self.red(0.5,0.5,0.5)
            self.red(0.5,0.5,1.5)
            self.red(0.5,2.5,2.5)
        elif(p == '1' and q=='0' and r=='1'):
            self.red(0.5,0.5,0.5)
            self.green(0.5,0.5,1.5)
            self.red(0.5,2.5,2.5)
        elif(p == '1' and q=='1' and r=='0'):
            self.red(0.5,0.5,0.5)
            self.red(0.5,0.5,1.5)
            self.green(0.5,2.5,2.5)
            # plt.show()
        elif(p == '0' and q=='1' and r=='1'):
            self.green(0.5,0.5,0.5)
            self.red(0.5,0.5,1.5)
            self.red(0.5,2.5,2.5)
            # plt.show()    
        elif(p == '1' and q=='0' and r=='0'):
            self.red(0.5,0.5,0.5)
            self.green(0.5,0.5,1.5)
            self.green(0.5,2.5,2.5)
            # plt.show()
        elif(p == '0' and q=='1' and r=='0'):
            self.green(0.5,0.5,0.5)
            self.red(0.5,0.5,1.5)
            self.green(0.5,2.5,2.5)
            # plt.show()
        elif(p == '0' and q=='0' and r=='1'):
            self.green(0.5,0.5,0.5)
            self.green(0.5,0.5,1.5)
            self.red(0.5,2.5,2.5)
            # plt.show()
        else:
            self.green(0.5,0.5,0.5)
            self.green(0.5,0.5,1.5)
            self.green(0.5,2.5,2.5)
            # plt.show()
        plt.show()
        return {"updated":"ok"}


    def red(self,x,y,z):
        global ax
        ax.scatter([x], [y], [z], color="r", s=1000)

    def green(self,x,y,z):
        global ax
        ax.scatter([x], [y], [z], color="g", s=1000)

# plt.show()

cherrypy.server.socket_host ='0.0.0.0' # put it here
cherrypy.config.update({'server.socket_port':8080,})
cherrypy.quickstart(layout())