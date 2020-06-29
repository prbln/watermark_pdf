import PyPDF2
import sys 
inputs = sys.argv[1:]
#opening and accessing the wtr-mark pg
reader1 = PyPDF2.PdfFileReader( open('watermark.pdf','rb') )
output = PyPDF2.PdfFileWriter()
#accessing each input pdf one by one
for pdf in inputs:
	reader = PyPDF2.PdfFileReader(open(pdf,'rb') )
	for page_no in range(reader.numPages):
		page = reader.getPage(page_no)
		page.mergePage(reader1.getPage(0))
		output.addPage(page)
		with open('water_super.pdf','wb') as new_file:
			output.write(new_file)
