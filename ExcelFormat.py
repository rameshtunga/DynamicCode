import xlwt

# cellProperties = {'fontSize': 12,
#                   'fontStyle': 'Times New Roman',
#                   # 'cellFontColor':'green',
#                   # 'cellBackGroundColor': 'red',
#                   # 'cellBorderLeft': None,
#                   # 'cellBorderRight': None,
#                   # 'cellBorderTop': None,
#                   # 'cellPatern': 'solid',
#                   'cellBorderBottom': 'thin',
#                   # 'cellBackGroundColor':'blue',
#                     'fontBold': False
#                   'wrapText': False
#                   }

def cellStyle(cellProperties = None):
    if cellProperties is None:
        return None
    fmt = xlwt.Style.easyxf(f'''
            font: name {cellProperties.get('fontStyle', 'Arial')}, 
                  height {cellProperties.get('fontSize', 12) * 20}, 
                  color {cellProperties.get('cellFontColor', '0')},
                  bold {cellProperties.get('fontBold', False)};
             
            borders: left {cellProperties.get('cellBorderLeft', '0')},
                     right {cellProperties.get('cellBorderRight', '0')},
                     top {cellProperties.get('cellBorderTop', '0')},
                     bottom {cellProperties.get('cellBorderBottom','0')};
            alignment:wrap {cellProperties.get('wrapText', False)},
                      horizontal {cellProperties.get('text_horizontal_alignment', 'general')},
                      vertical {cellProperties.get('text_vertical_alignment', 'bottom')};
            pattern: pattern {cellProperties.get('cellPatern', '0')}, fore_colour {cellProperties.get('cellForeColor', '0')},
            back_color {cellProperties.get('cellBackGroundColor', '0')};
            ''')
    return fmt

def highlightColumn(cellProperties = None, color=None):
    if color is not None:
        cellProperties['cellBackGroundColor'] = color
        cellProperties['cellPatern'] = 'solid'
        cellProperties['cellForeColor'] = color
        return cellStyle(cellProperties = cellProperties)
    else:
        return cellStyle(cellProperties = cellProperties)

def customizedCell(sheetName, rowNumber, colNumber, value, style = None):
    if style is None:
        sheetName.row(rowNumber).write(colNumber, value)
    else:
        sheetName.row(rowNumber).write(colNumber, value, style)








































# cellProperties = {'fontSize': 12,
#                   'fontStyle': 'Times New Roman',
#                   # 'cellFontColor':'green',
#                   # 'cellBackGroundColor': 'red',
#                   # 'cellBorderLeft': None,
#                   # 'cellBorderRight': None,
#                   # 'cellBorderTop': None,
#                   # 'cellPatern': 'solid',
#                   'cellBorderBottom': 'thin',
#                   # 'cellBackGroundColor':'blue'
#                   }



# def ExcelFormat(sheetName, rowNumber, colNumber, value, cellProperties):
#     """"""
#     book = xlwt.Workbook()
#     sheet = book.add_sheet("PySheet1")
#
#     cols = ["A", "B", "C", "D", "E"]
#     txt = "Row %s, Col %s"
#
#
#     for rowNumber in range(5):
#         for colNumber, col in enumerate(cols):
#             customizedCell(sheet, rowNumber, colNumber, 'kiran', cellProperties)
#
#
#     book.save("test3.xls")
#
# if __name__ == "__main__":
#     main()