import xlsxwriter

workbook = xlsxwriter.Workbook('/Users/meowmini/.openclaw/workspace/dev_projects/edca_simulator/assets/EDCA_Journal_Template.xlsx')
worksheet = workbook.add_worksheet('EDCA_Journal')

# Formats
header_format = workbook.add_format({'bold': True, 'bg_color': '#1E293B', 'font_color': 'white', 'align': 'center', 'valign': 'vcenter', 'border': 1})
dash_label_format = workbook.add_format({'bold': True, 'align': 'right', 'font_size': 12})
dash_value_format = workbook.add_format({'bold': True, 'bg_color': '#F8FAFC', 'border': 1, 'font_size': 12, 'num_format': '#,##0.00'})
dash_value_btc = workbook.add_format({'bold': True, 'bg_color': '#F8FAFC', 'border': 1, 'font_size': 12, 'num_format': '0.00000000'})
dash_value_pct = workbook.add_format({'bold': True, 'bg_color': '#F8FAFC', 'border': 1, 'font_size': 12, 'num_format': '0.00%'})
input_format = workbook.add_format({'bg_color': '#FEF3C7', 'border': 1})
input_date_format = workbook.add_format({'bg_color': '#FEF3C7', 'border': 1, 'num_format': 'dd-mmm-yyyy'})
input_num_format = workbook.add_format({'bg_color': '#FEF3C7', 'border': 1, 'num_format': '#,##0.00'})
calc_num_format = workbook.add_format({'bg_color': '#F1F5F9', 'border': 1, 'num_format': '#,##0.00'})
calc_btc_format = workbook.add_format({'bg_color': '#F1F5F9', 'border': 1, 'num_format': '0.00000000'})
note_format = workbook.add_format({'border': 1})

# Column widths
worksheet.set_column('A:A', 8)
worksheet.set_column('B:B', 15)
worksheet.set_column('C:C', 18)
worksheet.set_column('D:D', 18)
worksheet.set_column('E:E', 20)
worksheet.set_column('F:F', 18)
worksheet.set_column('G:G', 20)
worksheet.set_column('H:H', 18)
worksheet.set_column('I:I', 30)

# Dashboard (Rows 1-7)
worksheet.merge_range('A1:I1', 'EDCA Sniper - Investment Journal', workbook.add_format({'bold': True, 'font_size': 16, 'bg_color': '#3730A3', 'font_color': 'white', 'align': 'center'}))

worksheet.write('C3', 'ราคา BTC ปัจจุบัน ($):', dash_label_format)
worksheet.write('D3', 71000, dash_value_format) # Input current price
worksheet.write('E3', '<-- อัปเดตราคาที่นี่เพื่อดูพอร์ต', workbook.add_format({'italic': True, 'font_color': '#64748B'}))

worksheet.write('C4', 'จำนวน BTC สะสมรวม:', dash_label_format)
worksheet.write_formula('D4', '=SUM(E9:E1000)', dash_value_btc)

worksheet.write('C5', 'ทุนสะสมรวม ($):', dash_label_format)
worksheet.write_formula('D5', '=SUM(C9:C1000)', dash_value_format)

worksheet.write('C6', 'มูลค่าพอร์ตปัจจุบัน ($):', dash_label_format)
worksheet.write_formula('D6', '=D4*D3', dash_value_format)

worksheet.write('C7', 'กำไรสุทธิ ($):', dash_label_format)
worksheet.write_formula('D7', '=D6-D5', dash_value_format)

worksheet.write('C8', 'คิดเป็น %:', dash_label_format)
worksheet.write_formula('D8', '=IF(D5>0, (D6-D5)/D5, 0)', dash_value_pct)

# Table Headers (Row 10)
headers = ['งวดที่', 'วันที่ลงทุน', 'เงินลงทุนต่องวด ($)', 'ราคาที่ซื้อ ($)', 'จำนวน BTC ที่ได้', 'ทุนสะสม ($)', 'BTC สะสมรวม', 'ต้นทุนเฉลี่ย ($)', 'หมายเหตุ']
for col_num, data in enumerate(headers):
    worksheet.write(9, col_num, data, header_format)

# Add 500 rows of formulas
for i in range(10, 510):
    row_idx = i + 1
    worksheet.write(i, 0, f'=IF(C{row_idx}="","",ROW()-10)', calc_num_format) # งวดที่
    worksheet.write_blank(i, 1, '', input_date_format) # วันที่
    worksheet.write_blank(i, 2, '', input_num_format) # เงินลงทุน
    worksheet.write_blank(i, 3, '', input_num_format) # ราคาซื้อ
    worksheet.write_formula(i, 4, f'=IF(OR(ISBLANK(C{row_idx}),ISBLANK(D{row_idx}),D{row_idx}=0), "", C{row_idx}/D{row_idx})', calc_btc_format) # BTC ที่ได้
    worksheet.write_formula(i, 5, f'=IF(C{row_idx}="","",SUM($C$11:C{row_idx}))', calc_num_format) # ทุนสะสม
    worksheet.write_formula(i, 6, f'=IF(E{row_idx}="","",SUM($E$11:E{row_idx}))', calc_btc_format) # BTC สะสม
    worksheet.write_formula(i, 7, f'=IF(G{row_idx}="", "", IF(G{row_idx}>0, F{row_idx}/G{row_idx}, ""))', calc_num_format) # ทุนเฉลี่ย
    worksheet.write_blank(i, 8, '', note_format) # หมายเหตุ

# Add sample data for the first row to guide users
worksheet.write(10, 1, '01-Jan-2024', input_date_format)
worksheet.write(10, 2, 500, input_num_format)
worksheet.write(10, 3, 42000, input_num_format)

# Freeze panes
worksheet.freeze_panes(10, 0)

workbook.close()
