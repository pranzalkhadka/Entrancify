import camelot

tables = camelot.read_pdf('/home/pranjal/Downloads/Entrancify/Sample.pdf')
# tables = camelot.read_pdf('/home/pranjal/Downloads/Entrancify/Sample.pdf', pages='1-end')

tables.export('foo.csv', f='csv', compress=True)