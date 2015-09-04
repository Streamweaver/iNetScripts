from openpyxl import load_workbook
## Mappings
event_type_headers = (
    'event_type',
    'code', # int
    'event_type', # string, required
    'description', # string
    'priority', # int, required
    'agency_type',
    'disposition_required', # 1 or 0
    'recommendable', # 1 or 0
    'prior_radius',
    'recent_radius',
    'recent_expiry',
    'eqa_alias',
    'event_type_abbrev',
    'dispatch_group',
    'agencyid',
    )


## Methods
def write_csv(data, fieldmap, filename):
    """
    Writes a csv file to filename using a list in data to a csv export
    with headers dict fieldmap
    """
    return false

def read_original(filename, sheet):
    """Reads the xlsx spreadsheet from 'filename' and data from 'sheet'"""
    wb = load_workbook(filename)
    ws = wb.get_sheet_by_name(sheet)
    data = []
    for row in ws.rows:
        data.append([cell.value for cell in row]))
    return data


if __name__ == "__main__":
    read_original("raw_units.xlsx", "APCO types edited")
