import time
from data_parser.xlsx_parser import parse_cian_data


def process_result(result, excel_format):
    parsed = parse_cian_data(result)
    file_name = 'saved_%s' % int(time.time())
    if excel_format:
        parsed.to_excel('%s.xlsx' % file_name, encoding='utf-8-sig')
    else:
        parsed.replace(to_replace=[r"\\t|\\n|\\r|\,|\;", "\t|\n|\r|,|;"], value=[" ", " "], regex=True, inplace=True)
        parsed.to_csv('%s.csv' % file_name, encoding='utf-8-sig', index=False)
