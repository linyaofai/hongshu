# _*_coding:utf-8_*_
import pdfkit
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfdevice import PDFDevice
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal, LAParams
from pdfminer.pdfpage import PDFTextExtractionNotAllowed

url = "https://g.hongshu.com/content/93416/13877912.html"
pdfkit.from_url(url,"out.pdf")    #用wkhtmltopdf转换html为pdf

def parse(Path, Save_name):
    '''
    pdf转换为txt
    '''
    parser = PDFParser(Path)
    document = PDFDocument(parser)

    if not document.is_extractable:
        raise PDFTextExtractionNotAllowed
    else:
        rsrcmgr = PDFResourceManager()
        laparams = LAParams()
        device = PDFPageAggregator(rsrcmgr, laparams=laparams)
        interpreter = PDFPageInterpreter(rsrcmgr, device)

        for page in PDFPage.create_pages(document):
            interpreter.process_page(page)
            layout = device.get_result()
            for x in layout:
                if (isinstance(x, LTTextBoxHorizontal)):
                    with open('%s' % (Save_name), 'a') as f:
                        results = x.get_text().encode('utf-8').decode("utf-8")
                        print(results)
                        f.write(results + "\n")
                        # f.write(str(results.encode('utf-8').strip() + b"\n"))


if __name__ == '__main__':
    Path = open('out.pdf', 'rb')
    parse(Path, 'out.txt')