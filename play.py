import webapp2

class MainPage(webbapp2.RequestHandler):
	def get(self):
		self.response.headers['Content-Type'] = 'text/plain'
		self.response.out.write('Hello, webapp World!')

app = webapp2.WSGIApplication([('/', MainPage)], debug=True)
