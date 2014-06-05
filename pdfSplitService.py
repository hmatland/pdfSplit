import web
import os
from pdfSplit import split_pages
from pdfSplit import delete_pdfs

urls = (
	'/pdfsplit','split',
	'/pdf/(.*)','pdf'
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
		x = web.input(myfile={})
		directory = '/var/pdfSplit/pdf' # change this to the directory you want to store the file in.
		if 'myfile' in x: # to check if the file-object is created
			filename = x['myfile'].filename
			if('.pdf' in filename):
				fout = open(directory +'/'+ filename,'w') # creates the file where the uploaded file should be stored
				fout.write(x.myfile.file.read()) # writes the uploaded file to the newly created file.
				fout.close() # closes the file, upload complete.
				split_pages(directory +'/'+ filename,directory +'/splitted_'+ filename)
				raise web.seeother('/pdf/splitted_'+ filename)


		raise web.notfound()


class pdf:
	def GET(self,name):
		extension = name.split('.')[-1]
		if name in os.listdir('pdf'):
			web.header('Content-Type', 'application/pdf')
			pdf = open('pdf/%s' %name, 'rb').read()
			delete_pdfs(name)
			return pdf
		else:
			raise web.notfound()



if __name__ == '__main__':
	app.run()

