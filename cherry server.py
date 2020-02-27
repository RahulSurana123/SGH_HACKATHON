import cherrypy
import request
class full(object):
    @cherrypy.expose
    def __index__(self):
        self.hi = 5
        print("highdfgknkldnfvls")
        return
    # def yo(self) :
    @cherrypy.expose
    def yo(self):
        self.hi = 5

        print("highdfgknkldnfvls")
        return {"rahul":"ok"}


cherrypy.server.socket_host = '0.0.0.0' # put it here
cherrypy.config.update({'server.socket_port':8080,})
cherrypy.quickstart(full())