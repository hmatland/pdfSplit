import web

urls = (
	'/pdfsplit','split'
)

app = web.application(urls,globals())

class split:
	def GET(self):
		return """<html><head></head><body>
<form method="POST" enctype="multipart/form-data" action="">
<input type="file" name="myfile" />
<br/>
<input type="submit" />
</form>
</body></html>"""

	def POST(self):
		file = web.input(myfile={})
		return "filename: " + x['myfile'].filename

if __name__ == '__main__':
	app.run()