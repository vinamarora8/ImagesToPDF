from os import listdir, remove, getcwd
from PIL import Image
from pyPdf import PdfFileReader, PdfFileWriter

#Make a list of all files in the directory
full_dir = listdir('.')

#User input asking which file extension to be added to the pdf
extension = raw_input("File extension of images: ")

#Add all the files that have the same extension to a list
#Also create a list of these files (with a .pdf extension) to be used later
images = []
pdfs = []
for i in range (0, len(full_dir)):
	cur = full_dir[i]
	if cur[-len(extension):] == extension:
		images.append(Image.open(cur))
		pdfs.append(cur[:-len(extension)] + 'pdf')
		print "Opening File: " + cur
print ""

#Check if something weird has happened
if len(images) != len(pdfs):
	exit("Images and PDFs arrays have different lengths")

#Setup the final output object and a list for pages (will be populated later)
output = PdfFileWriter()
pages = []

#Save these images as pdfs, append then to the final output and delete the files
for i in range (0, len(images)):
	images[i].save(pdfs[i])
	print "Converting to pdf as: " + pdfs[i]
	pages.append(PdfFileReader(file(pdfs[i], "rb")))
	output.addPage(pages[i].getPage(0))
	remove(pdfs[i])
print ""

#Save the final output pdf in a file named as Current_Directory.pdf
output_file_name = getcwd().split('/')[-1] + ".pdf"
print "Saving the pdf: " + output_file_name
outputStream = file(output_file_name, "wb")
output.write(outputStream)

#Say GoodBye
print ""
print "It is done. Farewell"
