import xlrd
import xlwt

book = xlwt.Workbook()
sheet1 = book.add_sheet("sample")
 

book.save("test.xls")

book = xlrd.open_workbook("Global Edge.xlsx")

print book.nsheets
 
print book.sheet_names()

# get the first worksheet
first_sheet = book.sheet_by_index(0)
 
# read a row
print first_sheet.row_values(2)
