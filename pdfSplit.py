import copy
import math
import pyPdf
import os

def delete_pdfs(name):
  os.remove("pdf/"+name)
  os.remove("pdf/splitted_"+name)

def split_pages(src, dst):
  src_f = file(src, 'r+b')
  dst_f = file(dst, 'w+b')
  input = pyPdf.PdfFileReader(src_f)
  output = pyPdf.PdfFileWriter()

  for i in range(input.getNumPages()):
    page1 = input.getPage(i)
    page2 = copy.copy(page1)
    page2.mediaBox = copy.copy(page1.mediaBox)

    #x1,y2--x2,y2
    #|          |
    #|          |
    #x1,y3--x2,y3
    #|          |
    #|          |
    #x1,y1--x2,y1
    #x1,y2---x3,y2---x2,y2
    #|         |         |
    #|         |         |
    #|         |         |
    #x1,y1---x3,y1---x2,y1
    x1, y1 = page1.mediaBox.lowerLeft
    x2, y2 = page1.mediaBox.upperRight

    x1, y1 = math.floor(x1), math.floor(y1)
    x2, y2 = math.floor(x2), math.floor(y2)
    x3, y3 = math.floor(x2/2), math.floor(y2/2)

    if x2 < y2:
      # vertical
      page1.mediaBox.upperRight = (x2, y2)
      page1.mediaBox.lowerLeft = (x1, y3)
      page2.mediaBox.upperRight = (x2, y3)
      page2.mediaBox.lowerLeft = (x1, y1)
    else:
      # horizontal
      page1.mediaBox.upperRight = (x3, y2)
      page1.mediaBox.lowerLeft = (x1, y1)
      page2.mediaBox.upperRight = (x2, y2)
      page2.mediaBox.lowerLeft = (x3, y1)

    output.addPage(page1)
    output.addPage(page2)
  output.write(dst_f)
  src_f.close()
  dst_f.close()
