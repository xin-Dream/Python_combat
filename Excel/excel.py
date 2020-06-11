import openpyxl
import pprint
from PIL import Image

if __name__ == '__main__':
    wb = openpyxl.load_workbook("Excel/test1.xlsx")
    print(wb.get_sheet_names())
                                                    
    