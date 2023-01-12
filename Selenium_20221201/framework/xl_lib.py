from xlrd import open_workbook

def read_locators(sheetname):
    objects = { }
    wb = open_workbook("../data_files/objects.xls")
    ws = wb.sheet_by_name(sheetname)
    # "nrows" returns total number of used rows in the excel
    rows = ws.nrows
    for i in range(1, rows):   # range(1, 4)
        data = ws.row_values(i)
        objects[data[0]] = (data[1], data[2])
    return objects


def read_headers(sheetname, testcasename):
    wb = open_workbook("../data_files/testdata.xls")
    ws = wb.sheet_by_name(sheetname)
    rows = ws.nrows
    for i in range(0, rows):   # range(0, 16)
        temp = ws.row_values(i)
        if temp[0] == testcasename:
            # the row number of the testcase will be one less than the row where actual testdata is starting
            headers = ws.row_values(i-1)
            _headers = [ item for item in headers if item.strip() ]
            _headers = ",".join(_headers[2:])
            return _headers
            
def read_data(sheetname, testcasename):
    wb = open_workbook("../data_files/testdata.xls")
    ws = wb.sheet_by_name(sheetname)
    rows = ws.nrows
    final_data = [ ]
    for i in range(0, rows):   # range(0, 16)
        temp = ws.row_values(i)
        if temp[0] == testcasename:
            data = ws.row_values(i)
            data = [ item for item in data if item ]
            data = [ item for item in data if data[1] == "Yes" ]
            if data:
                final_data.append(tuple(data[2:]))
    return final_data
























































