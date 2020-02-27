import cherrypy
class full(object):
    hi=4
    def yo(self):
        self.hi=5
        return self.hi
cherrypy.server.socket_host = '0.0.0.0' # put it here
cherrypy.quickstart(full())