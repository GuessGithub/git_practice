
# Write contents from one excel to another


import xlrd


from xlutils.copy import copy

def xls_to_xls(src,des):
    
    rb_tar = xlrd.open_workbook(des,formatting_info=True)# xlsx to be written
    #   Note that formatting=True works for xls not xlsx
    des_pre = des.split('.',1)[0]


    rb_ori = xlrd.open_workbook(src)   # xlsx for data
    sheet_ori = rb_ori.sheet_by_index(0)    # Get the shee reference to use

    wb = copy(rb_tar)

    sheet_tar = wb.get_sheet(0)


    for i_tar in range(5,8):
        #sheet_tar.write(i_tar,1,sheet_ori.cell(i_tar-5,1).value)
        #sheet_tar.write(i_tar,2,sheet_ori.cell(i_tar-5,2).value)
        #sheet_tar.write(i_tar,3,sheet_ori.cell(i_tar-5,3).value)
        sheet_tar.write(i_tar,i_tar-4,sheet_ori.cell(i_tar,i_tar-5).value)

    new_name = des_pre + ".new.xls"

    wb.save(new_name)

xls_to_xls('demo2.xlsx','demo.xls')
print('Congratulations!')
